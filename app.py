from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)


@app.route('/cursos')
def cursos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT c.id, c.nombre, c.descripcion, COUNT(e.id) AS total_estudiantes
        FROM cursos c
        LEFT JOIN estudiantes e ON e.curso_id = c.id
        GROUP BY c.id
    """)
    cursos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('cursos.html', cursos=cursos)

@app.route('/cursos/create', methods=['GET', 'POST'])
def crear_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cursos (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('cursos'))
    return render_template('create.html')

@app.route('/cursos/edit/<int:id>', methods=['GET', 'POST'])
def editar_curso(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cursor.execute("UPDATE cursos SET nombre=%s, descripcion=%s WHERE id=%s", (nombre, descripcion, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('cursos')) 
    cursor.execute("SELECT * FROM cursos WHERE id=%s", (id,))
    curso = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit.html', curso=curso)

@app.route('/cursos/delete/<int:id>')
def eliminar_curso(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cursos WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('cursos'))



@app.route('/estudiantes')
def estudiantes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT e.id, e.nombre, e.correo, c.nombre AS curso
        FROM estudiantes e
        LEFT JOIN cursos c ON e.curso_id = c.id
    """)
    estudiantes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('estudiantes.html', estudiantes=estudiantes)

@app.route('/estudiantes/create', methods=['GET', 'POST'])
def crear_estudiante():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre FROM cursos")
    cursos = cursor.fetchall()

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        curso_id = request.form['curso_id']
        cursor.execute(
            "INSERT INTO estudiantes (nombre, correo, curso_id) VALUES (%s, %s, %s)",
            (nombre, correo, curso_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('estudiantes'))

    cursor.close()
    conn.close()
    return render_template('estcreate.html', cursos=cursos)

@app.route('/estudiantes/edit/<int:id>', methods=['GET', 'POST'])
def editar_estudiante(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre FROM cursos")
    cursos = cursor.fetchall()

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        curso_id = request.form['curso_id']
        cursor.execute(
            "UPDATE estudiantes SET nombre=%s, correo=%s, curso_id=%s WHERE id=%s",
            (nombre, correo, curso_id, id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('estudiantes'))

    cursor.execute("SELECT * FROM estudiantes WHERE id=%s", (id,))
    estudiante = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('estedit.html', estudiante=estudiante, cursos=cursos)

@app.route('/estudiantes/delete/<int:id>')
def eliminar_estudiante(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('estudiantes'))


if __name__ == '__main__':
    app.run(debug=True)

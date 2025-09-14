from flask import Flask, render_template, request

fr = Flask(__name__)

@fr.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        return render_template('response.html', nombre=nombre, correo=correo)
    return render_template('form.html')


if __name__ =='__main__':
    fr.run(debug=True)


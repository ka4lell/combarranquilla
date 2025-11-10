from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import Usuario
from app import db, login_manager

# Definimos el Blueprint
auth_bp = Blueprint('auth', __name__)

# =========================
# LOGIN
# =========================
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Usuario.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Credenciales inválidas.', 'danger')

    return render_template('login.html')


# =========================
# REGISTRO
# =========================
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        rol = request.form.get('rol', 'voluntario')  # Por defecto voluntario

        if Usuario.query.filter_by(email=email).first():
            flash('El correo ya está registrado.', 'warning')
        else:
            hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = Usuario(nombre=nombre, email=email, password=hashed_pw, rol=rol)
            db.session.add(new_user)
            db.session.commit()
            flash('Usuario registrado con éxito. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')


# =========================
# LOGOUT
# =========================
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('auth.login'))


# =========================
# CARGAR USUARIO
# =========================
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

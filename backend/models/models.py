from flask_login import UserMixin
from datetime import datetime
from app import db

# =========================
# TABLA: USUARIOS
# =========================
class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum('administrador', 'coordinador', 'voluntario'), nullable=False)

    # Relaciones
    actividades = db.relationship('Actividad', backref='voluntario', lazy=True)
    asistencias = db.relationship('Asistencia', backref='voluntario', lazy=True)
    certificados = db.relationship('Certificado', backref='voluntario', lazy=True)

    def get_id(self):
        return str(self.id_usuario)


# =========================
# TABLA: EVENTOS
# =========================
class Evento(db.Model):
    __tablename__ = 'eventos'

    id_evento = db.Column(db.Integer, primary_key=True)
    nombre_evento = db.Column(db.String(150), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    lugar = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    capacidad = db.Column(db.Integer)

    # Relaciones
    actividades = db.relationship('Actividad', backref='evento', lazy=True)
    asistencias = db.relationship('Asistencia', backref='evento', lazy=True)
    certificados = db.relationship('Certificado', backref='evento', lazy=True)


# =========================
# TABLA: ACTIVIDADES
# =========================
class Actividad(db.Model):
    __tablename__ = 'actividades'

    id_actividad = db.Column(db.Integer, primary_key=True)
    id_evento = db.Column(db.Integer, db.ForeignKey('eventos.id_evento'), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    hora_inicio = db.Column(db.DateTime)
    hora_fin = db.Column(db.DateTime)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))


# =========================
# TABLA: ASISTENCIAS
# =========================
class Asistencia(db.Model):
    __tablename__ = 'asistencias'

    id_asistencia = db.Column(db.Integer, primary_key=True)
    id_evento = db.Column(db.Integer, db.ForeignKey('eventos.id_evento'), nullable=False)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    estado = db.Column(db.Enum('asistio', 'no_asistio'), nullable=False)
    hora_registro = db.Column(db.DateTime, default=datetime.utcnow)


# =========================
# TABLA: CERTIFICADOS
# =========================
class Certificado(db.Model):
    __tablename__ = 'certificados'

    id_certificado = db.Column(db.Integer, primary_key=True)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_evento = db.Column(db.Integer, db.ForeignKey('eventos.id_evento'), nullable=False)
    horas_trabajadas = db.Column(db.Integer)
    archivo_pdf = db.Column(db.String(255))
    fecha_emision = db.Column(db.Date, default=datetime.utcnow)

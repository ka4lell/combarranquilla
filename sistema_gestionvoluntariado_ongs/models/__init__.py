from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import Usuario, Evento, Actividad, Asistencia, Certificado
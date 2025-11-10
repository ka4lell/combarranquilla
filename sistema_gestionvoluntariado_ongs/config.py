import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "clave-super-segura-kalel"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@localhost/proyectofinal"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

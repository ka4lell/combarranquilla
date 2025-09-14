import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # cambia por tu usuario
        password="",        # cambia por tu contraseña
        database="institutoo"  # cambia por tu base de datos
    )

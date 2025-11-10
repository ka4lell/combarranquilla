from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Inicializamos las extensiones
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # ruta a donde redirige si no hay sesión

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializamos las extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Importar modelos aquí (para que SQLAlchemy los reconozca)
    from models.models import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Importar y registrar los blueprints
    from routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    # (más adelante añadiremos event_routes y volunteer_routes)
    
    return app


# Punto de entrada
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

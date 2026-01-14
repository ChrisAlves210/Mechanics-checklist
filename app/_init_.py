from app.extensions import db
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        from app import routes
        from authentication.routes import auth as auth_blueprint

        app.register_blueprint(auth_blueprint, url_prefix='/auth')

        db.create_all()

    return app
app = create_app()
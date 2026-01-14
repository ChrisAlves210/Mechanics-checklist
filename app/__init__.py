from flask import Flask
from .extensions import db, login_manager


def create_app(config: dict = None) -> Flask:
    app = Flask(__name__, template_folder="../templates")

    # Base config
    app.config.update(
        SECRET_KEY="dev-secret-key",
        SQLALCHEMY_DATABASE_URI="sqlite:///mechanics_checklist.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if config:
        app.config.update(config)

    # Init extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from .models import User

    @login_manager.user_loader
    def load_user(user_id: str):
        return db.session.get(User, int(user_id))

    # Blueprints
    from app.routes import auth
    app.register_blueprint(auth)
    from app.main.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

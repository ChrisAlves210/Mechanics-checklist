from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Define instances only; initialize them in create_app()
db = SQLAlchemy()
login_manager = LoginManager()




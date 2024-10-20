from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  


    db.init_app(app)
    migrate = Migrate(app, db)


    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  

    from .models import User  


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    from app.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

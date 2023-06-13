from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    # Google Cloud SQL (change this accordingly)
    PASSWORD ="1234567"
    PUBLIC_IP_ADDRESS ="34.101.191.19"
    DBNAME ="database"
    PROJECT_ID ="login-389703"
    INSTANCE_NAME ="healthdiary"

    app.config["SECRET_KEY"] = "healthdiary secretkey"
    app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{1234567}@{34.101.191.19}/{database}?unix_socket =/cloudsql/{login-389703}:{health
}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Diary
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('web/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


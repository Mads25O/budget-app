from flask import Flask
import sqlalchemy

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "fucktrump"

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
from flask import Flask
from .routes import main_route as routes_main


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # config
    # app.config['SECRET_KEY'] = 'dev-key'

    app.register_blueprint(routes_main)

    return app

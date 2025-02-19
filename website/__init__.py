from flask import Flask
from .views import main_blueprint


# Code directly taken from Naser's Flask-to-do-List
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)

    # # check if testing app, to configure the app for testing
    # if os.environ.get('CONFIG_TYPE') == 'config.TestingConfig':
    #     app.config['SECRET_KEY'] = 'secret'
    # else:
    #     app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    return app


if __name__ == '__main__':
    create_app()
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options #importing config_options from config.py

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app



        # initial layout

# from config import DevConfig
# #innitializing the app
# app = Flask(__name__,instance_relative_config = True)# creating an app instance and passing the variable __name__
#
# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')
#
# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)
#
# from app.main import views, error

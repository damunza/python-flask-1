from flask import Flask

#innitializing the app
app = Flask(__name__)# creating an app instance and passing the variable __name__

from app import views

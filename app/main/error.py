from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOfour.html'),404



      #initial layout

# from app import app
#
# @app.errorhandler(404)
# def four_Ow_four(error):
#     '''
#     Function to render the 404 error page
#     '''
#     return render_template('fourOfour.html'),404
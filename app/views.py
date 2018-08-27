from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    function that returns the index page and its data
    '''
    message = 'Hi World'
    return render_template('index.html', message = message)# left message = variable in the template ; right message = variable in the function

# @app.route('/movie/<movie_id>')
# def movie(movie_id):
#
#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     return render_template('movie.html',id = movie_id)

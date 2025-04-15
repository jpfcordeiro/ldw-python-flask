#importando flask do pacote API
from api import app, mongo

from api.models.movieModel import Movie
from api.services import movieService

if __name__ == '__main__':
    with app.app_context():
        if 'movies' not in mongo.db.list_collection_names():
            movie = Movie(title='', year=0, description='')
            movieService.add_movie(movie)
    app.run(host='localhost',port='5000',debug=True)
from api import mongo
from bson.objectid import ObjectId

def add_movie(movie):
    result = mongo.db.movies.insert_one({
        'title': movie.title,
        'description': movie.description,
        'year': movie.year
    })  
    newMovie = mongo.db.movies.find_one({'_id': result._id})
    return newMovie
    
@staticmethod
def get_movies():
    return list(mongo.db.movies.find())

def getMovie(movie_id):
    return mongo.db.movies.find_one({'_id': ObjectId(movie_id)})

@staticmethod
def delete_movie(movie_id):
    mongo.db.movies.delete_one({'_id': ObjectId(movie_id)})

from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#Configurando flask com mongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/api-movies'

# Initialize extensions
ma = Marshmallow(app)
api = Api(app)
mongo = PyMongo(app)

# Initialize Marshmallow after app is created
ma.init_app(app)

# Import and register routes after all extensions are initialized
from .resources.movies_resources import MovieList, MovieDetail
api.add_resource(MovieList, '/movies')
api.add_resource(MovieDetail, '/movie/<movie_id>')

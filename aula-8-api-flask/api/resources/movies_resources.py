#importando a classe Resource do flask_restful
from flask_restful import Resource
from flask import make_response, jsonify, request
from ..schemas import movieSchema
from ..models import movieModel
from ..services import movieService

class MovieList(Resource):
    def get(self):
        movies = movieService.get_movies()
        mv = movieSchema.MovieSchema(many=True)
        
        return make_response(mv.jsonify(movies), 200)
    
    def post(self):
        mv = movieSchema.MovieSchema()
        validate = mv.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            title = request.json['title']
            year = request.json['year']
            description = request.json['description']
            newMovie = movieModel.Movie(title = title, year = year, description = description)
            result = movieService.add_movie(newMovie)
            res = mv.jsonify(result)
            return make_response(res, 201)


class MovieDetail(Resource):
    def delete(self, movie_id):
        movie = movieService.getMovie(movie_id)
        if movie is None:
            return make_response(jsonify({'message': 'Movie not found'}), 404)
        movieService.delete_movie(movie_id)
        return make_response(jsonify({'message': 'Movie deleted'}), 200)

    def get(self, movie_id):
        movie = movieService.getMovie(movie_id)
        if movie is None:
            return make_response(jsonify({'message': 'Movie not found'}), 404)
        mv = movieSchema.MovieSchema()
        res = mv.jsonify(movie)
        return make_response(res, 200)

    def put(self, movie_id):
        movie = movieService.getMovie(movie_id)
        if movie is None:
            return make_response(jsonify({'message': 'Movie not found'}), 404)
        mv = movieSchema.MovieSchema()
        validate = mv.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            title = request.json['title']
            year = request.json['year']
            description = request.json['description']
            newMovie = movieModel.Movie(title = title, year = year, description = description)
            result = movieService.update_movie(movie_id, newMovie)
            res = mv.jsonify(result)
            return make_response(res, 200)
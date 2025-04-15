from api import mongo

class Movie():
    def __init__(self, title, year, description):
        self.title = title
        self.description = description
        self.year = year

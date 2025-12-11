import csv
from fastapi import FastAPI

app = FastAPI()


class Movie:
    def __init__(self, movie_id, title, genres):
        self.movieId = movie_id
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id


class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp


def read_csv_data(filename, class_model):
    data_list = []
    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                objects = class_model(*row)
                data_list.append(objects)
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {filename}")
        return []

    return data_list


@app.get("/hello")
def hello():
    return {'hello': 'world'}


@app.get("/movies")
def get_movies():
    movies = read_csv_data('movies.csv', Movie)
    return [movie.__dict__ for movie in movies]


@app.get("/links")
def get_links():
    links = read_csv_data('links.csv', Link)
    return [link.__dict__ for link in links]


@app.get("/ratings")
def get_ratings():
    ratings = read_csv_data('ratings.csv', Rating)
    return [rating.__dict__ for rating in ratings]


@app.get("/tags")
def get_tags():
    tags = read_csv_data('tags.csv', Tag)
    return [tag.__dict__ for tag in tags]

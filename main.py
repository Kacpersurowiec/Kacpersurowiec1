import sqlite3
import csv
import os
from fastapi import FastAPI

DB_NAME = "movies.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        movieId INTEGER PRIMARY KEY,
        title TEXT,
        genres TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS links (
        movieId INTEGER PRIMARY KEY,
        imdbId TEXT,
        tmdbId TEXT,
        FOREIGN KEY(movieId) REFERENCES movies(movieId)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userId INTEGER,
        movieId INTEGER,
        rating REAL,
        timestamp INTEGER,
        FOREIGN KEY(movieId) REFERENCES movies(movieId)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userId INTEGER,
        movieId INTEGER,
        tag TEXT,
        timestamp INTEGER,
        FOREIGN KEY(movieId) REFERENCES movies(movieId)
    )
    """)

    conn.commit()

    cursor.execute("SELECT count(*) FROM movies")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    if os.path.exists('movies.csv'):
        with open('movies.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            to_db = [(row['movieId'], row['title'], row['genres']) for row in reader]
            cursor.executemany("INSERT INTO movies (movieId, title, genres) VALUES (?, ?, ?)", to_db)

    if os.path.exists('links.csv'):
        with open('links.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            to_db = [(row['movieId'], row['imdbId'], row['tmdbId']) for row in reader]
            cursor.executemany("INSERT INTO links (movieId, imdbId, tmdbId) VALUES (?, ?, ?)", to_db)

    if os.path.exists('tags.csv'):
        with open('tags.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            to_db = [(row['userId'], row['movieId'], row['tag'], row['timestamp']) for row in reader]
            cursor.executemany("INSERT INTO tags (userId, movieId, tag, timestamp) VALUES (?, ?, ?, ?)", to_db)

    if os.path.exists('ratings.csv'):
        with open('ratings.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            batch = []
            for row in reader:
                batch.append((row['userId'], row['movieId'], row['rating'], row['timestamp']))
                if len(batch) >= 5000:
                    cursor.executemany("INSERT INTO ratings (userId, movieId, rating, timestamp) VALUES (?, ?, ?, ?)",
                                       batch)
                    batch = []
            if batch:
                cursor.executemany("INSERT INTO ratings (userId, movieId, rating, timestamp) VALUES (?, ?, ?, ?)",
                                   batch)

    conn.commit()
    conn.close()


init_db()

app = FastAPI()


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/movies")
def get_movies():
    conn = get_db_connection()
    movies = conn.execute("SELECT * FROM movies").fetchall()
    conn.close()
    return movies


@app.get("/links")
def get_links():
    conn = get_db_connection()
    links = conn.execute("SELECT * FROM links").fetchall()
    conn.close()
    return links


@app.get("/tags")
def get_tags():
    conn = get_db_connection()
    tags = conn.execute("SELECT * FROM tags").fetchall()
    conn.close()
    return tags


@app.get("/ratings")
def get_ratings():
    conn = get_db_connection()
    ratings = conn.execute("SELECT * FROM ratings LIMIT 100").fetchall()
    conn.close()
    return ratings

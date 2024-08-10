import json
import os

def extract_movies(filename):
    movies = []
    with open(filename, 'r') as f:
        for line in f:
            filename, movie_name = line.strip().split(' ', 1)
            movies.append({'filename': filename, 'movie_name': movie_name})
    return json.dumps(movies)

print(extract_movies('movies.txt'))

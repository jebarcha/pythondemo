import json
from pathlib import Path

# movies = [
#     {"id": "1", "title": "A hard day's night", "year": 1964},
#     {"id": "2", "title": "Help", "year": 1965}
# ]

# data = json.dumps(movies)
# # print(data)
# Path("movies.json").write_text(data)

# -------
data = Path("movies.json").read_text()
movies = json.loads(data)  # we will get an array of dictionaries
print(movies)
print(movies[0])  # get the first item (movie)
print(movies[0]["title"])  # get the title of the fist movie

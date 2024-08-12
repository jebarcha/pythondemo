import sqlite3
import json
from pathlib import Path

# read all the movies.json
# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# save that list in a database
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()


# read from the db ----------------------
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)  # returns a cursor (iterable object)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)  # [(1, "A hard day's night", 1964), (2, 'Help', 1965)]

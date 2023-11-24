import mysql.connector

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

cursor = db.cursor()

#Select all the fields for the studio table
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()

print("-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

print()

#Select all the fields for the genre table
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()

print("-- DISPLAYING Genre RECORDS --")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

print()

#Select the movie names for those movies that have a runtime of less than 2 hours
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120")
filmRuntimes =  cursor.fetchall()

print("-- Displaying Short Film RECORDS --")
for filmRuntime in filmRuntimes:
    print("Film Name: {}\nRuntime: {}\n".format(filmRuntime[0], filmRuntime[1]))

print()

#Get a list of film names and directors ordered by director
cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director ")
filmDirectors = cursor.fetchall()

print("-- DISPLAYING Director RECORDS in Order --")
for filmDirector in filmDirectors:
    print("Film Name: {}\nDirector: {}\n".format(filmDirector[1], filmDirector[0]))
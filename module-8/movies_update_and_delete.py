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

def show_films(cursor, title):
    cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS "
                   "'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON "
                   "film.studio_id=studio.studio_id")
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film [2], film [3]))

show_films(cursor, "DISPLAYING FILMS")

cursor.execute("INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)"
               " VALUES (4, 'Gone Girl', 2014, 149, 'David Fincher', 1, 3)")

show_films(cursor, "DISPLAYING FILMS")

cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")

show_films(cursor, "DISPLAYING FILMS")

cursor.execute("DELETE FROM film WHERE film_id = 1")

show_films(cursor, "DISPLAYING FILMS")


# Jacob Ambrose 02/17/2024
# Module 8.2

# imports mysql connector
import mysql.connector
from mysql.connector import errorcode



# defines user login information
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# connects to database
try:
    db  = mysql.connector.connect(**config)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))   
    
    input("\n\n Press any key to continue... ")
    print('\n \n \n')
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)
        
finally:
    db.close()
    
    
# connect db to cursor
db = mysql.connector.connect(**config)
cursor = db.cursor()  
    
def show_films(cursor, title):
    cursor.execute("SELECT film_name as Name, film_director AS Director, genre_name as Genre, studio_name as 'Studio NAME' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    
    films = cursor.fetchall()
    
    print("\n -- {} --".format(title))
    
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))
        
 
# insert new film(s)
def add_films(cursor, title):
    sql= "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val=("Insidious", 2010, 101, "James Wan", 2, 1)
    cursor.execute(sql,val)

    cursor.execute("SELECT film_name as Name, film_director AS Director, genre_name as Genre, studio_name as 'Studio NAME' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    films = cursor.fetchall()
    
    print("\n -- {} --".format(title))
    
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))
   
        

# update movie ALIEN from scifi to horror
def update_films(cursor, title):
    cursor.execute("UPDATE film SET film.genre_id = '1' WHERE film.film_name = 'Alien' ")
    
    cursor.execute("SELECT film_name as Name, film_director AS Director, genre_name as Genre, studio_name as 'Studio NAME' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    genre_update = cursor.fetchall()
    
    
    print("\n -- {} -- Changed Alien to Horror".format(title))
    
    for x in genre_update:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(x[0], x[1], x[2], x[3]))



# delete movie Gladiator from table
def delete_films(cursor, title):
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator' ")
    cursor.execute("SELECT film_name as Name, film_director AS Director, genre_name as Genre, studio_name as 'Studio NAME' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    
    films = cursor.fetchall()
    
    print("\n -- {} --".format(title))
    
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

        
show_films(cursor, 'DISPLAYING FILMS')
add_films(cursor, "DISPLAYING FILMS AFTER INSERT")
update_films(cursor, "DISPLAYING FILMS AFTER UPDATE--")
delete_films(cursor, 'DISPLAYING FILMS AFTER DELETE')
    
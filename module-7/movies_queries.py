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



# creates cursor execution method
db = mysql.connector.connect(**config)
cursor = db.cursor()

# Runs query to select all fields for the STUDIO table
cursor.execute("SELECT studio_id,studio_name FROM studio")

studio = cursor.fetchall()

# prints heading
print("\n-- DISPLAYING studio RECORDS -- \n")

# prints output
for x in studio:
    print("Studio ID: ", x[0])
    print("Studio Name: ", x[1])


# Runs query to select all fields for the GENRE table
cursor.execute("SELECT * FROM genre")

genre = cursor.fetchall()

# prints heading
print("\n-- DISPLAYING genre RECORDS -- \n")

# prints output

for x in genre:
    print("Genre ID: ", x[0])
    print("Genre Name: ", x[1])
    


# Runs query to provide movie names where movies have a runtime of less than 2 hours
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

short_film = cursor.fetchall()

# prints heading
print("\n-- DISPLAYING short film RECORDS -- \n")

# prints output

for x in short_film:
    print("Film Name:   ", x[0])
    print("Runtime:   ", x[1], "minutes")
    
    
# Runs query to provide films in order of director name
cursor.execute("SELECT  film_name, film_director FROM film ORDER BY film_director")

director = cursor.fetchall()

# prints heading
print("\n-- DISPLAYING director RECORDS in Order -- \n")

# prints output

for x in director:
    print("Film Name:   ", x[0])
    print("Director:   ", x[1])
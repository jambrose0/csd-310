# Jacob Ambrose 02/17/2024
# Module 8.2

# imports mysql connector
import mysql.connector
from mysql.connector import errorcode



# defines user login information
config = {
    "user": "wilson_user",
    "password": "financial",
    "host": "127.0.0.1",
    "database": "bravo",
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
# db = mysql.connector.connect(**config)
# cursor = db.cursor()  
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
db = mysql.connector.connect(**config)

# TO-DO
# generate at least 3 reports
# report1: customers joined by month
# report3: customers with more than 10 transactions
# report4: total average number of assets SELECT AVG(column_name) FROM table_name WHERE condition;

# connect db to cursor
db = mysql.connector.connect(**config)
cursor = db.cursor() 


# counts average number of assets
def avg_assets(cursor, title):
    sql = "SELECT AVG (asset_value) FROM assets"
    cursor.execute(sql)
    
    asset_avg = cursor.fetchall()
    
    print("\n -- {} --\n".format(title))
    
    print("Average number of assets: ${}".format(asset_avg))


def new_clients(cursor, title):
    sql = "SELECT client_name, client_address, client_phone, client_email, client_startDate FROM client WHERE client_startDate >= DATE_SUB(NOW(), INTERVAL 6 MONTH)"
    cursor.execute(sql)
    
    
    clients = cursor.fetchall()
    print("\n -- {} --\n".format(title))
    
    for row in clients:
        print("Client Name: {}\nClient Address: {}\nClient Phone: {}\nClient Email: {}\nClient Since: {}\n".format(row[0], row[1], row[2], row[3], row[4]))
    


new_clients(cursor, 'THE FOLLOWING CLIENT(S) HAVE JOINED WITHIN THE PAST 6 MONTHS')
# avg_assets(cursor, 'REPORTING AVERAGE NUMBER OF ASSETS')
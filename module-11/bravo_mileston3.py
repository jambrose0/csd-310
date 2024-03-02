# Jacob Ambrose 02/17/2024
# Module 8.2
# report1: Average assets
# report2: customers with more than 10 transactions
# report3: New customers obtained with last 6 months

# imports mysql connector
import mysql.connector
from mysql.connector import errorcode
from datetime import date

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

today = date.today()
# connect db to cursor
db = mysql.connector.connect(**config)
cursor = db.cursor()


#average assets report
def avg_assets(cursor, title):
    print("--{} Managed by Willson Financial--".format(avg_assets))
    cursor.execute("SELECT AVG (asset_value) FROM transactions")
    avg_asset_value = cursor.fetchone()[0] 
    print("\n -- {} --\n".format(title))
    print("**Report Generated On: ",today, "**\n")
    print("Assets Value: {}".format(avg_asset_value))



#customers with more than 10 transactions 
def big_spenders(cursor, title):
    print("\n -- {} --\n".format(title))
    print("**Report Generated On: ",today, "**")
    cursor.execute(""" SELECT c.Client_ID, c.CLIENT_NAME, COUNT(*) AS TransactionCount 
        FROM transactions t 
        JOIN CLIENTS c ON t.Client_ID = c.Client_ID 
        GROUP BY c.Client_ID, c.CLIENT_NAME 
        HAVING TransactionCount > 10""")
    rows = cursor.fetchall()
    for client_id, client_name, transaction_count in rows:
        print("Client ID: {}\nClient Name: {}\nTransaction Count: {}\n".format(client_id, client_name, transaction_count))
    print("\n")
    
#customers joined last 6 months
def new_clients(cursor, title):
    print("\n -- {} --\n".format(title))

    cursor.execute("""SELECT 
            YEAR(Client_StartDate) AS Year,
            MONTH(Client_StartDate) AS Month,
            CLIENT_NAME,
            COUNT(*) AS NewClients
        FROM 
            CLIENTS
        WHERE 
            Client_StartDate >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
        GROUP BY 
            YEAR(Client_StartDate), MONTH(Client_StartDate), CLIENT_NAME
        ORDER BY 
            Year, Month;""")
    results = cursor.fetchall()
    print("Clients Added for Each of the Past Six Months:")
    print("Year\tMonth\tClient Name\tNew Clients")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

    print("**Report Generated On: ",today, "**")


avg_assets(cursor, 'REPORTING AVERAGE NUMBER OF ASSETS')
big_spenders(cursor, 'CUSTOMERS WITH MORE THAN 10 TRANSACTIONS')
new_clients(cursor, "CLIENTS ADDED WITHIN THE PAST 6 MONTHS:")


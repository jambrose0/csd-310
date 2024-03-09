#team Bravo - Milestone 5 
#Module 12.2 changing the assets report
# report1: Average assets
# report2: customers with more than 10 transactions
# report3: New customers obtained with last 6 months

from datetime import date
today = date.today()


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Frogg3r$2839",
    "host": "127.0.0.1",
    "database": "team_bravo",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

#average assets report
avg_assets = "Average Assets"
print("--{} Managed by Willson Financial--\n".format(avg_assets))
print("** Report Generated On: ", today, "**\n")

# Execute a query to calculate the overall average of all assets
cursor.execute("SELECT AVG(asset_value) FROM transactions")
overall_avg_asset_value = cursor.fetchone()[0]
formatted_overall_avg_asset_value = "${:,.2f}".format(overall_avg_asset_value)
print("Overall Average Asset Value: {}\n".format(formatted_overall_avg_asset_value))

# Execute a query to get the average value of each asset type
cursor.execute("SELECT Asset_Type, AVG(asset_value) AS AvgAssetValue FROM transactions t JOIN assets a ON t.Asset_ID = a.Asset_ID GROUP BY Asset_Type")
avg_assets_breakdown = cursor.fetchall()

# Prepare data for tabulation
asset_data = []
for asset_type, avg_asset_value in avg_assets_breakdown:
    formatted_avg_asset_value = "${:,.2f}".format(avg_asset_value)
    asset_data.append([asset_type, formatted_avg_asset_value])

# Import the tabulate module
from tabulate import tabulate

# Define the headers
head = ["Asset Type", "Average Value"]

# Display the table using the tabulate module
print(tabulate(asset_data, headers=head, tablefmt="grid"))

print("\n")



#customers with more than 10 transactions 
customer_transaction = "Customers with more than 10 transactions"
print("-- {} --".format(customer_transaction))
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
last_6months = "New Clients in the past 6 months"
print("--{}--".format(last_6months))

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






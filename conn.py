import mysql.connector

# Replace these values with your MySQL server and database information
db_config = {
    "host": "shopify.clkyu9vsrxwy.eu-north-1.rds.amazonaws.com",
    "user": "admin",
    "password": "ajit5455"
}


# Establish a connection to the MySQL server
connection = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Execute a simple query (e.g., fetching version)
# cursor.execute("SELECT VERSION()")

# # Fetch and print the result
# data = cursor.fetchone()
# print(f"MySQL Database Version: {data[0]}")
# product_data = {
#     "title": "The Archived Snowboard",
#     "body_html": "This is a gift card for the store",
#     "vendor": "Snowboard Vendor",
#     "status": "archived",
#     "price": 20.00,
#     "stock": 20
# }

# insert_query = "INSERT INTO product (title, body_html, vendor,status,price,stock) VALUES (%(title)s, %(body_html)s, %(vendor)s, %(status)s, %(price)s, %(stock)s)"

# cursor.execute(insert_query, product_data)

# Commit the changes to the database
connection.commit()
  



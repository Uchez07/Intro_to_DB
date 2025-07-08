import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="alx_boook_store"
)

print("Database", 'alx_book_store' ,"created successfully!")

conn.close()
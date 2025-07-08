import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="alx_boook_store"
    )


    if connection.is_connected():
        cursor = connection.cursor()

        # Try to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
    print("Error while connecting to MySQL:", e)

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
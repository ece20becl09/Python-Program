import mysql.connector
from mysql.connector import Error

connection = None
cursor = None

try:
    # Connect to MySQL
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="NewStrongPassword123!",
        database="ashim"
    )

    if connection.is_connected():
        print("✅ Connected Successfully!")

        # Create a cursor
        cursor = connection.cursor()

        # Execute SQL query
        cursor.execute("SELECT DATABASE(), CURRENT_USER(), VERSION()")

        # Fetch one row
        database_name, mysql_user, mysql_version = cursor.fetchone()

        print("Database :", database_name)
        print("MySQL User :", mysql_user)
        print("MySQL Version :", mysql_version)

except Error as e:
    print("❌ Error:", e)

finally:
    # Close cursor
    if cursor is not None:
        cursor.close()

    # Close connection
    if connection is not None and connection.is_connected():
        connection.close()
        print("Connection Closed")
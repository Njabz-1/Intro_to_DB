import mysql.connector
from mysql.connector import Error

def create_database():
    """Create MySQL database if it does not exist."""
    try:
        # Connect to the MySQL Server
        connection = mysql.connector.connect(
            host='localhost',       # Or your host, e.g., '127.0.0.1'
            user='your_username',   # Your MySQL username
            password='your_password'  # Your MySQL password
        )
        if connection.is_connected():
            # Create cursor to execute SQL statements
            cursor = connection.cursor()
            # Create database using a SQL statement
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
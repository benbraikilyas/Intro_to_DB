import mysql.connector
from mysql.connector import Error

# Function to create database
def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',  # Change to your MySQL server host if necessary
            user='root',       # Change to your MySQL username
            password='password'  # Change to your MySQL password
        )

        # Check if connection is successful
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        else:
            print("Failed to connect to the database server.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Run the function to create the database
create_database()

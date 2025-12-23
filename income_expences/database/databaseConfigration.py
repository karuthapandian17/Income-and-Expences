import mysql.connector
from mysql.connector import Error

def create_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("connection is closed")

def create_database():
    connection = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            database_name = "income_expenses"

            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            
            cursor.execute(f"USE {database_name}")
            print(f"$Database '{database_name}' has used")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    fullname VARCHAR(100)  NOT NULL,
                    email VARCHAR(100) UNIQUE  NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("Users table created successfully")
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    name VARCHAR(100) NOT NULL,
                    type ENUM('income', 'expense') NOT NULL,              
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("Categories table created successfully")
            return connection
    except Error as e:
        print(f"Error: '{e}'")

    if __name__ == "__main__":
        db_connection = create_database()       
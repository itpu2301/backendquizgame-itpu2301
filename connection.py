import mysql.connector
import logging

# Define the database connection parameters
dbConfig = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'quizgame'
}

# Configure logging
logging.basicConfig(level=logging.INFO)  # You can adjust the log level as needed

# Function to establish a connection
def getConnection():
    try:
        connection = mysql.connector.connect(**dbConfig)
        return connection
    except mysql.connector.Error as error:
        logging.error("Error: %s", error)
        return None

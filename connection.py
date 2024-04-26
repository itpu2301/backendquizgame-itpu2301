import mysql.connector

# Define the database connection parameters
dbConfig = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'quizgame'
}

# Function to establish a connection
def getConnection():
    try:
        connection = mysql.connector.connect(**dbConfig)
        return connection
    except mysql.connector.Error as error:
        print("Error:", error)
        return None

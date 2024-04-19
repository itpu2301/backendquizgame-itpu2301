
import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',      # MySQL host
    user='root',  # MySQL username
    password='1234',  # MySQL password
    database=''  # MySQL database name
)

# Connect to the MySQL database
if connection.is_connected():
    print('Connected to MySQL database')

# Function to fetch all questions from the database
def get_all_questions():
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM questions'
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as error:
        print('Error fetching questions:', error)
        return None

# Function to close the connection to the MySQL database
def close_connection():
    if connection.is_connected():
        connection.close()
        print('Connection to MySQL database closed')

# Example usage:
# questions = get_all_questions()
# print(questions)

# Close the connection to the MySQL database
# close_connection()
##
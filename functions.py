import logging
import mysql.connector
from connection import getConnection

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level as needed

def getRandomQuestion():
    connection = getConnection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            # Query for a random question
            cursor.execute("SELECT * FROM questions ORDER BY RAND() LIMIT 1")
            randomQuestion = cursor.fetchone()
            return randomQuestion
        except mysql.connector.Error as error:
            logging.error("Error occurred: %s", error)  # Log the error
            return None
        finally:
            if cursor:
                cursor.close()
            connection.close()
    else:
        return None

if __name__ == "__main__":
    randomQuestion = getRandomQuestion()
    if randomQuestion:
        logging.info("Random Question:")
        logging.info("ID: %s", randomQuestion['id'])
        logging.info("Difficulty: %s", randomQuestion['difficulty'])
        logging.info("Question: %s", randomQuestion['question'])
    else:
        logging.info("No questions found.")

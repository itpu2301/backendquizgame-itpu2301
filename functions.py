import logging
import mysql.connector
from connection import getConnection

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level as needed

def isCorrect(QuestionId, id):
    connection = getConnection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT is_correct FROM answers WHERE question_id = %s AND id = %s", (QuestionId, id))
            isCorrectBoolean = cursor.fetchone()
            if isCorrectBoolean and isCorrectBoolean["is_correct"] == 1:
                return True
            else:
                return False
    
        except mysql.connector.Error as error:
            logging.error("Error occurred: %s", error)
            return None
        finally:
            if cursor:
                cursor.close()
            connection.close()
    else:
        return None

def getRandomQuestionWithAnswers(difficulty):
    connection = getConnection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, question FROM questions WHERE difficulty = %s ORDER BY RAND() LIMIT 1", (difficulty,))
            randomQuestion = cursor.fetchone()
            if randomQuestion:
                cursor.execute("SELECT id, answer FROM answers WHERE question_id = %s", (randomQuestion['id'],))
                answers = cursor.fetchall()
                questionWithAnswers = {
                    "difficulty": difficulty,
                    "question": randomQuestion['question'],
                    "answers": answers,
                    "question_id": randomQuestion['id']
                }
                return questionWithAnswers
                
            else:
                logging.info("No questions found for difficulty level %s.", difficulty)
                return None
        except mysql.connector.Error as error:
            logging.error("Error occurred: %s", error)
            return None
        finally:
            if cursor:
                cursor.close()
            connection.close()
    else:
        return None


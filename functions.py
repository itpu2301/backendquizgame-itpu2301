import logging
import mysql.connector
from connection import getConnection

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level as needed

def isCorrect(QuestionId, answer):
    connection = getConnection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT is_correct FROM answers WHERE question_id = %s AND answer = %s", (QuestionId, answer))
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

def getRandomQuestionWithAnswers():
    connection = getConnection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, difficulty, question FROM questions ORDER BY RAND() LIMIT 1")
            randomQuestion = cursor.fetchone()
            if randomQuestion:
                cursor.execute("SELECT question_id, id, answer FROM answers WHERE question_id = %s", (randomQuestion['id'],))
                answers = cursor.fetchall()
                questionWithAnswers = {
                    "difficulty": randomQuestion['difficulty'],
                    "question": randomQuestion['question'],
                    "answers": answers
                }
                return questionWithAnswers
                
            else:
                logging.info("No questions found.")
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

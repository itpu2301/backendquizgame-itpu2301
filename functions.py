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
            cursor.execute("SELECT is_correct FROM answers  WHERE question_id = %s AND answer = %s",(QuestionId,answer))
            isCorrectBoolean = cursor.fetchone()
            if(isCorrectBoolean["is_correct"]==1):
                return True;
            else:
                return False;
    
        except mysql.connector.Error as error:
            logging.error("Error occurred: %s", error)  # Log the error
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
            # Select a random question
            cursor.execute("SELECT id, difficulty, question FROM questions ORDER BY RAND() LIMIT 1")
            randomQuestion = cursor.fetchone()
            if randomQuestion:
                # Fetch all answers for the selected question
                cursor.execute("SELECT answer, is_correct FROM answers WHERE question_id = %s", (randomQuestion['id'],))
                answers = cursor.fetchall()
                # Construct the array with difficulty, question, and answers
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
            logging.error("Error occurred: %s", error)  # Log the error
            return None
        finally:
            if cursor:
                cursor.close()
            connection.close()
    else:
        return None

if __name__ == "__main__":
    
    isCorrectValue = isCorrect(5,"Oktober")  # test aufruf von isCorrect
    randomQuestionWithAnswers = getRandomQuestionWithAnswers()
    if randomQuestionWithAnswers:
        print(randomQuestionWithAnswers)
        logging.info("Random Question:")
        logging.info("Difficulty: %s", randomQuestionWithAnswers['difficulty'])
        logging.info("Question: %s", randomQuestionWithAnswers['question'])
        logging.info("Answers:")
        print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",isCorrectValue) #langer dddd..string um es im terminal leichter zu finden
        
        for answer in randomQuestionWithAnswers['answers']:
            logging.info("- %s (Correct: %s)", answer['answer'], answer['is_correct'])
            
    else:
        logging.info("No questions found.")

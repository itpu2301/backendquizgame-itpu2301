import logging
import mysql.connector
from connection import getConnection

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level as needed

def getRandomQuestionWithAnswers():
    connection = getConnection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            # Select a random question
            cursor.execute("SELECT id, difficulty, question FROM questions ORDER BY RAND() LIMIT 1")
            random_question = cursor.fetchone()
            if random_question:
                # Fetch all answers for the selected question
                cursor.execute("SELECT answer, is_correct FROM answers WHERE question_id = %s", (random_question['id'],))
                answers = cursor.fetchall()
                # Construct the array with difficulty, question, and answers
                question_with_answers = {
                    "difficulty": random_question['difficulty'],
                    "question": random_question['question'],
                    "answers": answers
                }
                return question_with_answers
                
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
    
    random_question_with_answers = getRandomQuestionWithAnswers()
    if random_question_with_answers:
        print(random_question_with_answers)
        logging.info("Random Question:")
        logging.info("Difficulty: %s", random_question_with_answers['difficulty'])
        logging.info("Question: %s", random_question_with_answers['question'])
        logging.info("Answers:")
        
        for answer in random_question_with_answers['answers']:
            logging.info("- %s (Correct: %s)", answer['answer'], answer['is_correct'])
            
    else:
        logging.info("No questions found.")
    

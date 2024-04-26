
from connection import getConnection

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
            print("Error:", error)
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
        print("Random Question:")
        print("ID:", randomQuestion['id'])
        print("Difficulty:", randomQuestion['difficulty'])
        print("Question:", randomQuestion['question'])
    else:
        print("No questions found.")

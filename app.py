from flask import Flask, jsonify
import mysql.connector
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',      # MySQL host
    user='root',           # MySQL username
    password='12345678',   # MySQL password
    database='quizgame'    # MySQL database name
)

# Function to fetch all questions from the database
def getAllQuestions():
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM questions'
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as error:
        logging.error('Error fetching questions:', error)
        return None

# Route to get all questions
@app.route('/questions')
def getQuestions():
    questions = getAllQuestions()
    if questions is not None:
        return jsonify(questions), 200
    else:
        return jsonify({"error": "Failed to fetch questions"}), 500

# Function to fetch all answers from the database
def getAllAnswers():
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM answers'
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as error:
        logging.error('Error fetching answers:', error)
        return None

# Route to get all answers
@app.route('/answers')
def getAnswers():
    answers = getAllAnswers()
    if answers is not None:
        return jsonify(answers), 200
    else:
        return jsonify({"error": "Failed to fetch answers"}), 500

# Close the connection to the MySQL database when the application ends
@app.teardown_appcontext
def closeConnection(exception=None):
    if connection.is_connected():
        connection.close()
        logging.info('Connection to MySQL database closed')

if __name__ == '__main__':
    app.run(debug=True)

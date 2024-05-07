from flask import Flask, jsonify
from flask_cors import CORS
import logging
from functions import isCorrect, getRandomQuestionWithAnswers

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Configure logging
logging.basicConfig(level=logging.INFO)

# Route to check if an answer is correct
@app.route('/is_correct/<int:question_id>/<int:id>', methods=['GET'])
def checkAnswer(question_id, id):
    correct = isCorrect(question_id, id)
    if correct is not None:
        return jsonify({"correct": correct}), 200
    else:
        return jsonify({"error": "Failed to check answer"}), 500

# Route to get a random question with answers
@app.route('/random_question', methods=['GET'])
def getRandomQuestion():
    question = getRandomQuestionWithAnswers()
    if question is not None:
        return jsonify(question), 200
    else:
        return jsonify({"error": "Failed to get random question"}), 500

if __name__ == '__main__':
    app.run(debug=True)

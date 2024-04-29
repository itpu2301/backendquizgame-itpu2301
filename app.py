from flask import Flask, jsonify
import logging
from functions import isCorrect, getRandomQuestionWithAnswers

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Route to check if an answer is correct
@app.route('/is_correct/<int:question_id>/<answer>', methods=['GET'])
def check_answer(question_id, answer):
    correct = isCorrect(question_id, answer)
    if correct is not None:
        return jsonify({"correct": correct}), 200
    else:
        return jsonify({"error": "Failed to check answer"}), 500

# Route to get a random question with answers
@app.route('/random_question', methods=['GET'])
def get_random_question():
    question = getRandomQuestionWithAnswers()
    if question is not None:
        return jsonify(question), 200
    else:
        return jsonify({"error": "Failed to get random question"}), 500

if __name__ == '__main__':
    app.run(debug=True)

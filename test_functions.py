import logging
from quizGameBackend.score import getRandomQuestionWithAnswers
from unittest.mock import MagicMock, patch

# Mocken der getConnection-Funktion
@patch('functions.getConnection')
def test_getRandomQuestionWithAnswers(mock_getConnection):
    # Mocken der Verbindung
    mock_connection = MagicMock()
    mock_getConnection.return_value = mock_connection

    # Mocken des Cursors und der execute-Methode
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'id': 1, 'difficulty': 'easy', 'question': 'What is 1 + 1?'}
    mock_cursor.fetchall.return_value = [{'answer': '2', 'is_correct': True},
                                          {'answer': '3', 'is_correct': False},
                                          {'answer': '4', 'is_correct': False}]

    # Aufruf der zu testenden Funktion
    result = getRandomQuestionWithAnswers()

    # Überprüfen, ob das Ergebnis korrekt ist
    assert result == {
        "difficulty": "easy",
        "question": "What is 1 + 1?",
        "answers": [{'answer': '2', 'is_correct': True},
                    {'answer': '3', 'is_correct': False},
                    {'answer': '4', 'is_correct': False}]
    }

    # Überprüfen, ob die Verbindungsmethoden aufgerufen wurden
    mock_getConnection.assert_called_once()
    mock_connection.cursor.assert_called_once()
    mock_cursor.execute.assert_called()
    mock_cursor.fetchone.assert_called_once()
    mock_cursor.fetchall.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()

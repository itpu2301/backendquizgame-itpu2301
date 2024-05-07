import sys
sys.path.append('../')  # Passe den Pfad entsprechend deiner Verzeichnisstruktur an

import pytest
import mysql.connector
from unittest.mock import MagicMock, patch
from jocker import hasUserUsedJoker, addJokerEntry
from connection import dbConfig

# Mocking the mysql.connector.connect function
@patch('mysql.connector.connect')
def test_hasUserUsedJoker(mock_connect):
    # Mocking the cursor and its execute method
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = [1]  # Assuming the kandidat has already used the joker
    mock_connect.return_value.cursor.return_value = mock_cursor

    # Call the hasUserUsedJoker function
    result = hasUserUsedJoker("Testkandidat2")

    # Assertions
    assert result is True
    mock_connect.assert_called_once_with(**dbConfig)
    mock_cursor.execute.assert_called_once()

@patch('mysql.connector.connect')
def test_addJokerEntry(mock_connect):
    # Mocking the cursor
    mock_cursor = MagicMock()
    mock_connect.return_value.cursor.return_value = mock_cursor

    # Call the addJokerEntry function
    addJokerEntry("Testkandidat3")

    # Assertions
    mock_connect.assert_called_once_with(**dbConfig)
    mock_cursor.execute.assert_called_once()
    mock_cursor.execute.assert_called_with("INSERT INTO jocker (kandidat, used) VALUES (%s, %s)", ("Testkandidat3", 1))

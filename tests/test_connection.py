import unittest
import sys
from unittest.mock import MagicMock, patch
import mysql.connector
import logging

# Add the parent package directory to the Python path
sys.path.append("..")
from connection import getConnection  # Assuming connection.py is in the parent directory

class TestConnection(unittest.TestCase):
    
    @patch('mysql.connector.connect')
    def test_GetConnectionSuccess(self, mock_connect):
        # Mocking the successful connection
        mock_connection = MagicMock(spec=mysql.connector.connection.MySQLConnection)
        mock_connect.return_value = mock_connection

        # Calling the getConnection function
        conn = getConnection()

        # Assertions
        self.assertIsNotNone(conn)
        mock_connect.assert_called_once_with(host='localhost', user='root', password='12345678', database='quizgame')

    @patch('mysql.connector.connect')
    def test_GetConnectionFailure(self, mock_connect):
        # Mocking the connection failure
        mock_connect.side_effect = mysql.connector.Error("Connection error")

        # Calling the getConnection function
        with self.assertLogs(level=logging.ERROR):
            conn = getConnection()

        # Assertions
        self.assertIsNone(conn)

if __name__ == '__main__':
    unittest.main()

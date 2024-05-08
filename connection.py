import mysql.connector
import logging
import traceback
from config import dbConfig




# Function to establish a connection
def getConnection():
    try:
        connection = mysql.connector.connect(**dbConfig)
        return connection
    except mysql.connector.Error as error:
        logging.error("Error: %s", error)
        logging.error("Error Class: %s", error.__class__.__name__)
        logging.error("Traceback: %s", traceback.format_exc())
        return None


connection = getConnection()
if connection:
    try:
        
        cursor = connection.cursor()
       
    finally:
        connection.close()

import logging
import mysql.connector
from connection import getConnection
import datetime

def enterScores(candidate, score):
    connection = getConnection()
    if connection:
        try:
            cursor = connection.cursor()
            date= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO scores (user, score, date_added) VALUES (%s, %s, %s)", (candidate, score, date))
            connection.commit()
            return True
        except mysql.connector.Error as error:
            logging.error("Error occurred: %s", error)
            return False
        finally:
            connection.close()

def getScores():
    connection = getConnection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT user, score, date_added FROM scores")
            rows = cursor.fetchall()
            return rows
        except mysql.connector.Error as error:
            logging.error("Error occurred: %s", error)
            return []
        finally:
            connection.close()

# Usage example for enterScores:
# Assuming you want to insert a record for a player named "John" with a score of 600
if enterScores("John", 600):
    logging.info("Record inserted successfully!")
else:
    logging.info("Failed to insert record.")

# Usage example for getScores:
scores = getScores()
logging.info("+---------+-------+---------------------+")
logging.info("|  Name   | Score |     Date Added      |")
logging.info("+---------+-------+---------------------+")
for row in scores:
   logging.info("| {:<8} | {:>5} | {:^19} |".format(row[0], row[1], row[2]))
logging.info("+---------+-------+---------------------+")
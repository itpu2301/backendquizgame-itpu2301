import mysql.connector
from datetime import datetime
import logging
from connection import dbConfig



# Funktion zur Überprüfung, ob der Benutzer den Joker bereits verwendet hat
def hasUserUsedJoker(kandidat):
    try:
        connection = mysql.connector.connect(**dbConfig)
        cursor = connection.cursor()

        # Überprüfe, ob der Benutzer den Joker bereits verwendet hat
        query = "SELECT COUNT(*) FROM jocker WHERE kandidat = %s"
        cursor.execute(query, (kandidat,))
        count = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        # Wenn der Benutzer den Joker bereits verwendet hat, gib True zurück, sonst False
        return count > 0
    except mysql.connector.Error as error:
        logging.debug("Fehler beim Überprüfen des Jokers:", error)
        return False

# Funktion zum Hinzufügen eines Joker-Eintrags für einen Benutzer
def addJokerEntry(kandidat):
    try:
        connection = mysql.connector.connect(**dbConfig)
        cursor = connection.cursor()

        # Füge einen Eintrag für den Benutzer hinzu
        query = "INSERT INTO jocker (kandidat, used) VALUES (%s, %s)"
        cursor.execute(query, (kandidat, 1))  # Wir setzen 'used' hier auf 1, da der Joker verwendet wurde

        connection.commit()
        cursor.close()
        connection.close()

        logging.debug("Joker wurde erfolgreich hinzugefügt.")
    except mysql.connector.Error as error:
        logging.debug("Fehler beim Hinzufügen des Jokers:", error)

# Beispielaufruf der Funktionen
kandidat = "Ola"  # Beispiel-Kandidat
if not hasUserUsedJoker(kandidat):
    addJokerEntry(kandidat)
else:
    logging.debug("Der Kandidat hat den Joker bereits verwendet.")

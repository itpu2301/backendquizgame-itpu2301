from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Erstellen der Flask-App
app = Flask(__name__)

# 2. SQLAlchemy-Grundlagen einrichten
Base = declarative_base()

# 3. Verbindung zur MySQL-Datenbank herstellen
db_engine = create_engine("mysql+mysqlconnector://root:12345678@localhost:3306/quizgame")

# 4. Sessionmaker konfigurieren
Session = sessionmaker(bind=db_engine)

# 5. Datenbankmodell für die 'questions'-Tabelle
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)

# 6. Funktion zum Abrufen aller Fragen aus der Datenbank
def get_all_questions():
    # 6.1 Session erstellen
    session = Session()
    # 6.2 Alle Einträge aus der Tabelle 'questions' abfragen
    questions = session.query(Question).all()
    # 6.3 Session schließen
    session.close()
    # 6.4 Rückgabe als Liste von Dictionaries
    return [{'id': q.id, 'question': q.question} for q in questions]

# 7. Route zum Abrufen aller Fragen
@app.route('/questions', methods=['GET'])
def fetch_questions():
    questions = get_all_questions()  # 7.1 Abrufen der Fragen
    return jsonify(questions)  # 7.2 Rückgabe als JSON

# 8. Start der Flask-App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
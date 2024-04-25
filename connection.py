from sqlalchemy import create_engine, MetaData, Table, insert
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

#

def addUserScore(username, score, db_connection):
    try:
        # Reflecting the database tables
        metadata = MetaData()
        metadata.reflect(bind=db_connection)

        # Accessing the tables
        highscore_table = Table('highscore', metadata, autoload=True, autoload_with=db_connection)

        # Adding a new user with score
        new_user_score = {'user': username, 'score': score}
        db_connection.execute(insert(highscore_table).values(new_user_score))
        logging.info(f"User '{username}' with score '{score}' added successfully.")

    except Exception as e:
        logging.error(f"An error occurred while adding user score: {e}")

def clearUserScores(username, db_connection):
    try:
        # Reflecting the database tables
        metadata = MetaData()
        metadata.reflect(bind=db_connection)

        # Accessing the tables
        highscore_table = Table('highscore', metadata, autoload=True, autoload_with=db_connection)

        # Deleting user scores
        delete_statement = highscore_table.delete().where(highscore_table.c.user == username)
        db_connection.execute(delete_statement)
        logging.info(f"All scores for user '{username}' cleared successfully.")

    except Exception as e:
        logging.error(f"An error occurred while clearing user scores: {e}")

if __name__ == "__main__":
    db_engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/backend")

    # Example usage:
    addUserScore("steve", 500, db_engine)
    # clearUserScores("steve", db_engine)  # Uncomment this line to clear user scores

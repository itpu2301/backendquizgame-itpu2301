
#

from sqlalchemy import create_engine, MetaData, Table, insert

def add_user_score(username, score):
    try:
        # Creating the engine
        engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/backend")
        
        # Reflecting the database tables
        metadata = MetaData()
        metadata.reflect(bind=engine)

        # Accessing the tables
        highscore_table = Table('highscore', metadata, autoload=True, autoload_with=engine)

        # Establishing a connection
        with engine.connect() as connection:
            # Adding a new user with score
            new_user_score = {'user': username, 'score': score}
            connection.execute(insert(highscore_table).values(new_user_score))
            # Commit the transaction
            connection.commit()
            
            print(f"User '{username}' with score '{score}' added successfully.")

    except Exception as e:
        print("An error occurred:", e)

def clear_user_scores(username):
    try:
        # Creating the engine
        engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/backend")
        
        # Reflecting the database tables
        metadata = MetaData()
        metadata.reflect(bind=engine)

        # Accessing the tables
        highscore_table = Table('highscore', metadata, autoload=True, autoload_with=engine)

        # Establishing a connection
        with engine.connect() as connection:
            # Deleting user scores
            delete_statement = highscore_table.delete().where(highscore_table.c.user == username)
            connection.execute(delete_statement)
            
            # Commit the transaction
            connection.commit()
            
            print(f"All scores for user '{username}' cleared successfully.")

    except Exception as e:
        print("An error occurred:", e)




if __name__ == "__main__":
    # Example usage:
    add_user_score("steve", 500)
    #clear_user_scores()

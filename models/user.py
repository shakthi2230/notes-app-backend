import uuid
from database import get_connection
from datetime import datetime

class UserModel:

    @staticmethod
    def create_users_table(cursor):
        """
        Create the 'users' table if it does not exist.
        """
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id VARCHAR(36) PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                user_email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                last_update TIMESTAMP NOT NULL,
                create_on TIMESTAMP NOT NULL
            )
        """)


    @staticmethod
    def create_user(user_name, user_email, hashed_password):
        conn = get_connection()
        cursor = conn.cursor()
        user_id = str(uuid.uuid4())
        now = datetime.now()

        UserModel.create_users_table(cursor)
        
        cursor.execute(
            """
            INSERT INTO users (user_id, user_name, user_email, password, last_update, create_on)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (user_id, user_name, user_email, hashed_password, now, now)
        )
        conn.commit()
        conn.close()
        return user_id

    @staticmethod
    def find_user_by_email(email):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE user_email = %s", (email,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    @staticmethod
    def find_user_by_id(user_id):
        """
        Find a user by their user_id.
        """
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user
    

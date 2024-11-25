import uuid
from database import get_connection
from datetime import datetime

class NotesModel:

    @staticmethod
    def create_notes_table(cursor):
        """
        Create the 'notes' table if it does not exist.
        """
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                note_id VARCHAR(36) PRIMARY KEY,
                note_title VARCHAR(255) NOT NULL,
                note_content TEXT NOT NULL,
                user_id VARCHAR(36) NOT NULL,
                last_update TIMESTAMP NOT NULL,
                created_on TIMESTAMP NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)


    @staticmethod
    def create_note(user_id, note_title, note_content):
        conn = get_connection()
        cursor = conn.cursor()
        note_id = str(uuid.uuid4())
        now = datetime.now()
        NotesModel.create_notes_table(cursor)
        cursor.execute(
            """
            INSERT INTO notes (note_id, note_title, note_content, user_id, last_update, created_on)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (note_id, note_title, note_content, user_id, now, now)
        )
        conn.commit()
        conn.close()
        return note_id

    @staticmethod
    def get_notes_by_user(user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notes WHERE user_id = %s", (user_id,))
        notes = cursor.fetchall()
        conn.close()
        return notes
    
    @staticmethod
    def update_note(note_id, note_title, note_content):
        """
        Update an existing note's title and content based on the note_id.
        """
        conn = get_connection()
        cursor = conn.cursor()
        now = datetime.now()

        cursor.execute(
            """
            UPDATE notes
            SET note_title = %s, note_content = %s, last_update = %s
            WHERE note_id = %s
            """,
            (note_title, note_content, now, note_id)
        )

        conn.commit()
        conn.close()

        return {"note_id": note_id, "note_title": note_title, "note_content": note_content}
    
    @staticmethod
    def delete_note(note_id):
        """
        Delete a note by its note_id.
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM notes WHERE note_id = %s
            """,
            (note_id,)
        )

        conn.commit()
        conn.close()


   
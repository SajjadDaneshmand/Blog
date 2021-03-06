# internal
import functions

# standard
import sqlite3

def tables_creator():
    '''This function create a table of a blog database'''
    conn = functions.db_connection()
    cursor = conn.cursor()
    tables = [
        """
            CREATE TABLE IF NOT EXISTS category(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS post(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                category_id INTEGER NOT NULL
            )
        """
        ]
    for table in tables:
        cursor.execute(table)
    conn.commit()


if __name__ == '__main__':
    tables_creator()
import sqlite3
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

class DummyData:
    def __init__(self, app):
        super().__init__()

        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()

        # clean up tables from previous development run
        cursor.execute("delete from TODO")
        cursor.execute("delete from USERS")

        # insert dummy data into the user table
        user_records = [
            ("Colin But", "colin.but@email.com")
        ]
        user_query = 'insert into USERS (name, email) values (?, ?);'
        app.logger.info("Running query: {}".format(user_query))
        cursor.executemany(user_query, user_records)
        app.logger.info("Inserted {} records to the user table".format(cursor.rowcount))

        # insert dummy data into the todo table
        todo_records = [
            ("Title", "Description", False, False, 1)
        ]
        todo_query = 'insert into TODO (title, description, _is_done, _is_deleted, user_id) values (?,?,?,?,?)'
        app.logger.info("Running query: {}".format(todo_query))
        cursor.executemany(todo_query, todo_records)
        app.logger.info("Inserted {} records to the todo table".format(cursor.rowcount))

        conn.commit()
        conn.close()
import sqlite3
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

class DummyData:
    def __init__(self):
        super().__init__()

        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()

        records = [
            ("Colin But", "colin.but@email.com")
        ]

        query = 'insert into USERS (name, email) values (?, ?);'
        LOGGER.info("Running query: {}".format(query))

        cursor.executemany(query, records)

        LOGGER.info("Inserted {} records to the table".format(cursor.rowcount))

        conn.commit()
        conn.close()
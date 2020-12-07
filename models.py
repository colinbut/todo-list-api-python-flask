import sqlite3

class Schema:
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_todo_table()

    
    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
            _id INTEGER PRIMARY KEY,
            name TEXT,
            email EMAIL
        )
        """
        self.conn.execute(query)

    def create_todo_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            created_on Date DEFAULT CURRENT_DATE,
            due_data Date,
            user_id INTEGER FOREIGNKEY REFERENCES User(_id)
        )
        """
        self.conn.execute(query)

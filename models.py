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
            due_date Date,
            user_id INTEGER FOREIGNKEY REFERENCES User(_id)
        )
        """
        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description, user_id):
        query = f'insert into {TABLENAME} ' \
                f'(title, description, user_id) ' \
                f'values ("{text}","{description}", "{user_id}")'

        result = self.conn.execute(query)
        return result

    def update(self, text, description):
        query = f'update {TABLENAME} set title = {text}, description = {description}'

        result = self.conn.execute(query)
        return result

    def delete(self, id):
        query = f'update {TABLENAME} set _is_deleted = true'

        result = self.conn.execute(query)
        return result

    def select(self, user_id):
        query = f'select * from {TABLENAME} where user_id = "{user_id}"'

        result = self.conn.execute(query)

        return result


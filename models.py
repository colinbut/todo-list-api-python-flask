import sqlite3

class Schema:
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_todo_table()
        self.conn.close()

    
    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "USERS" (
            _id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
        """
        self.conn.execute(query)

    def create_todo_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "TODO" (
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

    def create(self, title, description, user_id):
        query = f'insert into {self.TABLENAME} ' \
                f'(title, description, user_id) ' \
                f'values ("{title}","{description}", "{user_id}")'

        print(query)

        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

    def update(self, title, description, todo_id):
        query = f'update {self.TABLENAME} set title = "{title}", description = "{description}" ' \
                f'where id = {todo_id}'

        print(query)
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

    def delete(self, id):
        query = f'update {self.TABLENAME} set _is_deleted = true where id = "{id}"'

        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

    def select_all(self, user_id):
        query = f'select * from {self.TABLENAME} where user_id = "{user_id}"'

        cursor = self.conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        result = []
        for row in results:
            result.append({
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "_is_done": bool(row[3]),
                "_is_deleted": bool(row[4]),
                "created_on": row[5],
                "due_date": row[6],
                "user_id": row[7]
            })

        return result

    def select(self, todo_id, user_id):
        query = f'select * from {self.TABLENAME} where user_id = "{user_id}" and id = "{todo_id}"'

        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        
        return {
            "id": result[0],
            "title": result[1],
            "description": result[2],
            "_is_done": bool(result[3]),
            "_is_deleted": bool(result[4]),
            "created_on": result[5],
            "due_date": result[6],
            "user_id": result[7]
        }


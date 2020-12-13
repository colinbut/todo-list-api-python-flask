import uuid
from models import ToDoModel

class ToDoService:
    def __init__(self):
        super().__init__()
        self.model = ToDoModel()
    
    def create_todo(self, params):
        self.model.create(params["title"], params["description"], params["user_id"])

    def update_todo(self, params):
        self.model.update(params["title"], params["description"], params["id"])

    def delete_todo(self, id):
        self.model.delete(id)

    def get_todos(self, user_id):
        return self.model.select_all(user_id)

    def get_todo(self, id, user_id):
        return self.model.select(id, user_id)

import uuid

class ToDoService:
    def __init__(self):
        super().__init__()
        self.model = ToDoModel()
    
    def create_todo(self, params):
        self.model.create(params["text"], params["description"], 1)

    def update_todo(self, params):
        self.model.update(params["text"], params["description"], 1)

    def delete_todo(self, id):
        self.model.delete(id)

    def get_todos(self, user_id):
        self.model.select(user_id)

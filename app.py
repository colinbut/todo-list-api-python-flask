from models import Schema
from setup import DummyData
from service import ToDoService
from flask import Flask, request
import logging

app = Flask(__name__)

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


@app.route("/todo", method=["GET"])
def list_todo():
    user_id = request.args.get('user_id')
    LOGGER.info("Retrieving list of todos for user: {}".format(user_id))

    return ToDoService().get_todos(user_id)


@app.route("/todo", method=["POST"])
def create_todo():
    return ToDoService().create(request.json())



if __name__ == "__main__":
    Schema()
    DummyData()
    app.run(debug=True, host='0.0.0.0', port=8888)
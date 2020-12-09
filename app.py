from models import Schema
from setup import DummyData
from service import ToDoService
from flask import Flask, request, Response
import logging

app = Flask(__name__)

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


@app.route("/todo", method=["GET"])
def list_todo():
    user_id = request.args.get('user_id')
    LOGGER.info("Retrieving list of todos for user: {}".format(user_id))

    todos = ToDoService().get_todos(user_id)
    LOGGER.info("Retrieved list of todos: {} for user: {}".format(todos, user_id))

    return Response("{}", status=200, mimetype="application/json")


@app.route("/todo", method=["POST"])
def create_todo():
    LOGGER.info("Creating new todo: {}".format(request.json()))
    ToDoService().create_todo(request.json())
    return Response("{}", status=201, mimetype="application/json")


@app.route("/todo", method=["PUT"])
def update_todo():
    LOGGER.info("Updating todo")
    ToDoService().update_todo(request.json())
    
    return Response("{}", status=204, mimetype="application/json")


@app.route("/todo/<id>", method=["DELETE"])
def delete_todo(id):
    LOGGER.info("Deleting todo with id: {}".format(id))
    ToDoService().delete_todo(id)
    LOGGER.info("Deleted todo with id: {}".format(id))
    return Response("{}", status=204, mimetype="application/json")


@app.route("/todo/<id>", method=["GET"])
def get_todo(id):
    user_id = request.args.get('user_id')
    LOGGER.info("Retrieving list of todos for user: {}".format(user_id))

    todo = ToDoService().get_todo(id, user_id)
    LOGGER.info("Retrieved todo: {} for user: {}".format(todo, user_id))

    return Response("{}", status=200, mimetype="application/json")


if __name__ == "__main__":
    Schema()
    DummyData()
    app.run(debug=True, host='0.0.0.0', port=8888)
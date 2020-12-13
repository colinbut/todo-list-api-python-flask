from models import Schema
from setup import DummyData
from service import ToDoService
from flask import Flask, request, Response, jsonify
import logging

app = Flask(__name__)


@app.route("/todo", methods=["GET"])
def list_todo():
    user_id = request.args.get('user_id')
    app.logger.info("Retrieving list of todos for user: {}".format(user_id))
    
    todos = ToDoService().get_todos(user_id)
    app.logger.info("Retrieved list of todos: {} for user: {}".format(todos, user_id))
    
    return jsonify(todos)


@app.route("/todo", methods=["POST"])
def create_todo():
    app.logger.info("Creating new todo: {}".format(request.json))
    ToDoService().create_todo(request.json)
    return Response("{}", status=201, mimetype="application/json")


@app.route("/todo", methods=["PUT"])
def update_todo():
    app.logger.info("Updating todo: {}".format(request.json))
    ToDoService().update_todo(request.json)
    
    return Response("{}", status=204, mimetype="application/json")


@app.route("/todo/<id>", methods=["DELETE"])
def delete_todo(id):
    app.logger.info("Deleting todo with id: {}".format(id))
    ToDoService().delete_todo(id)
    app.logger.info("Deleted todo with id: {}".format(id))
    return Response("{}", status=204, mimetype="application/json")


@app.route("/todo/<id>", methods=["GET"])
def get_todo(id):
    user_id = request.args.get('user_id')
    app.logger.info("Retrieving list of todos for user: {}".format(user_id))

    todo = ToDoService().get_todo(id, user_id)
    app.logger.info("Retrieved todo: {} for user: {}".format(todo, user_id))

    return jsonify(todo)


if __name__ == "__main__":
    Schema()
    DummyData(app)
    app.run(debug=True, host='0.0.0.0', port=8888)
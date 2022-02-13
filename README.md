# todo-list-api-python-flask

This example demonstrates building a Web API in Python using Python's Flask Web App Framework. 

## Running App locally
```bash
./start_app.sh
```

## Running App locally (Dockerized)

```bash
docker build -t todo-list-api-python-flask .
docker run -d -p 8888:8888 todo-list-api-python-flask:latest
```

By default the app is exposed on port `8888` (see `src/app.py`)

## API Endpoints

e.g.

```
curl http://localhost:8888/todo?user_id={user_id}
curl http://localhost:8888/todo/{todo_id}?user_id={user_id}

curl -X POST -H "Content-Type: application/json" -d "{ \"description\": \"Organize fixing of microwave\", \"title\": \"Fixing microwave\", \"user_id\": 1 }" http://localhost:8888/todo

curl -X PUT -H "Content-Type: application/json" -d "{ \"description\": \"Organize fixing of microwave\", \"title\": \"Fixing microwave\", \"user_id\": {user_id}, \"id: {todo_id}\" }" http://localhost:8888/todo


curl -X DELETE http://localhost:8888/todo/{todo_id}
```

## Author

Colin But.

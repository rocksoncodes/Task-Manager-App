from flask import Flask
from flask_cors import CORS
from api.task_routes import task

def create_app():
    task_app = Flask(__name__)
    CORS(task_app)
    task_app.register_blueprint(task, url_prefix="/api/tasks")
    return task_app

if __name__ == "__main__":
    task_app = create_app()
    task_app.run(debug=True, host="127.0.0.1", port=5000)
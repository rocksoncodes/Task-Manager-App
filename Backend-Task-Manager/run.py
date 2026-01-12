from flask import Flask
from api.task_routes import task

def create_app():
    app = Flask(__name__)
    app.register_blueprint(task, url_prefix="/api/tasks")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="127.0.0.1", port=5000)
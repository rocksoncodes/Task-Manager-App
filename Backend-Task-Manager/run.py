from flask import Flask
from flask_cors import CORS
from api.task_routes import task

def create_app():
    application = Flask(__name__)
    CORS(application)
    application .register_blueprint(task, url_prefix="/api/tasks")
    return application

if __name__ == "__main__":
    application  = create_app()
    application .run(debug=True, host="127.0.0.1", port=5000)
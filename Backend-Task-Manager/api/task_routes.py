from flask import Blueprint, request
from sqlalchemy.orm import sessionmaker
from database.database import database_engine
from api.task_controller import TaskController

task =  Blueprint("task", __name__)
Sessions = sessionmaker(bind=database_engine)

@task.route("/create/task", methods=["POST"])
def create_task_route():
    new_request = request.get_json()
    return TaskController.create_task(new_request)

@task.route("/get/tasks/all", methods=["GET"])
def get_all_tasks_route():
    return TaskController.get_all_tasks()


@task.route("/get/tasks/<task_status>", methods=["GET"])
def get_task_route(task_status):
   return TaskController.get_task(task_status)


@task.route("/get/completed/tasks/<completed>", methods=["GET"])
def get_completed_tasks_route(completed):
    return TaskController.get_completed_tasks(completed)


@task.route("/update/task/<task_id>", methods=["PUT"])
def update_task_route(task_id):
    return TaskController.update_task(task_id)


@task.route("/delete/task/<task_id>", methods=["DELETE"])
def delete_task_route(task_id):
    return TaskController.delete_task(task_id)

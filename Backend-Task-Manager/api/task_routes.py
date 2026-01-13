from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from database.database import database_engine
from database.models import Task

task =  Blueprint("task", __name__)
Sessions = sessionmaker(bind=database_engine)

@task.route("/create/task", methods=["POST"])
def create_task():
    post_data = request.get_json()

    try:
        with Sessions() as session:
            new_task = Task(
                title=post_data["title"],
                task_descriptions=post_data["task_descriptions"],
                task_status=post_data["task_status"],
                completed=post_data["completed"],
            )

            session.add(new_task)
            session.commit()

    except KeyError:
        return  jsonify({"error": "Missing required parameters"}), 400

    return jsonify({"message": "Task created successfully"}), 201


@task.route("/get/tasks/all", methods=["GET"])
def get_all_tasks():
    try:
        with Sessions() as session:
            all_tasks = session.query(Task).all()

            if not all_tasks:
                return jsonify({"message": "No tasks found"}), 404

            all_tasks_found = []
            for task_item in all_tasks:
                all_tasks_found.append({
                    "title": task_item.title,
                    "task_descriptions": task_item.task_descriptions,
                    "task_status": task_item.task_status,
                    "completed": task_item.completed,
                })

            return jsonify(all_tasks_found), 200

    except Exception as e:
            return jsonify({"error": str(e)}), 400


@task.route("/get/tasks/<task_status>", methods=["GET"])
def get_task(task_status):
    try:
        with Sessions() as session:
            task_stat = task_status
            specific_tasks = session.query(Task).filter(Task.task_status == task_stat).all()

            if not specific_tasks:
                return jsonify({"error": "Unable to find task"}), 404

            result = []

            for tasks in specific_tasks:
                result.append({
                    "title": tasks.title,
                    "task_descriptions": tasks.task_descriptions,
                    "task_status": tasks.task_status,
                    "completed": tasks.completed,
                })

            return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@task.route("/get/completed/tasks/<completed>", methods=["GET"])
def get_completed_tasks(completed):
    try:
        with Sessions() as session:
            task_completed = completed
            specific_tasks = session.query(Task).filter(Task.completed == task_completed).all()

            if not specific_tasks:
                return jsonify({"message": "no tasks completed tasks found"}), 200

            result = []

            for tasks in specific_tasks:
                result.append({
                    "title": tasks.title,
                    "task_descriptions": tasks.task_descriptions,
                    "task_status": tasks.task_status,
                    "completed": tasks.completed,
                })

            return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@task.route("/update/task/<task_id>", methods=["PUT"])
def update_task(task_id):
    put_data = request.get_json()

    try:
        with Sessions() as session:
            task_id = int(task_id)
            specific_task = session.get(Task, task_id)

            if not specific_task:
                return jsonify({"error": "Task not found"}), 404

            specific_task.title = put_data["title"]
            specific_task.task_descriptions = put_data["task_descriptions"]
            specific_task.task_status = put_data["task_status"]
            specific_task.completed = put_data["completed"]

            session.commit()

    except KeyError:
        return jsonify({"error": "Missing required parameters"}), 400

    return jsonify({"message": "Task updated successfully"}), 200


@task.route("/delete/task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        with Sessions() as session:
            task_id = int(task_id)
            specific_task = session.get(Task, task_id)

            if not specific_task:
                return jsonify({"error": "Task not found"}), 404

            session.delete(specific_task)
            session.commit()

            return jsonify({"message": "Task deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

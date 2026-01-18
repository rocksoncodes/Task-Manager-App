from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from database.database import database_engine
from database.models import Task

Sessions = sessionmaker(bind=database_engine)

class TaskController:
    """Controller class for Task CRUD operations."""

    @staticmethod
    def create_task(new_request):
        """Create a new task"""
        try:
            required_fields = ["title", "task_descriptions", "task_status", "completed"]

            for field in required_fields:
                if field not in new_request:
                    return jsonify({"error": f"Missing required parameter: {field}"}), 400

            with Sessions() as session:
                new_task = Task(
                    title=new_request["title"],
                    task_descriptions=new_request["task_descriptions"],
                    task_status=new_request["task_status"],
                    completed=new_request["completed"],
                )

                session.add(new_task)
                session.commit()

            return jsonify({"message": "Task created successfully"}), 201

        except KeyError:
            return jsonify({"error": "Missing required parameters"}), 400


    @staticmethod
    def get_all_tasks():
        """Fetch all tasks."""
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


    @staticmethod
    def get_task(task_status):
        """Fetch tasks filtered by status."""
        try:
            with Sessions() as session:
                task_stat = task_status
                specific_tasks = session.query(Task).filter(Task.task_status == task_stat).all()

                if not specific_tasks:
                    return jsonify({"error": "No tasks found with this status"}), 404

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


    @staticmethod
    def get_completed_tasks(completed):
        """Fetch tasks filtered by completion status."""
        try:
            with Sessions() as session:
                task_completed = completed
                specific_tasks = session.query(Task).filter(Task.completed == task_completed).all()

                if not specific_tasks:
                    return jsonify({"message": "No tasks completed tasks found"}), 404

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


    @staticmethod
    def update_task(task_id):
        """Update a task by ID."""
        try:
            put_data = request.get_json()

            required_fields = ["title", "task_descriptions", "task_status", "completed"]
            for field in required_fields:
                if field not in put_data:
                    return jsonify({"error": f"Missing required parameter: {field}"}), 400

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

            return jsonify({"message": "Task updated successfully"}), 200

        except KeyError:
            return jsonify({"error": "Missing required parameters"}), 400


    @staticmethod
    def delete_task(task_id):
        """Delete a task by ID."""
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
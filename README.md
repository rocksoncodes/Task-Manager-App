# Task Manager App

An Angular-based task manager application currently under development, paired with a Flask backend API. This project is intended for learning, testing and contributions.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Node.js** (v16+ recommended)
* **npm** (v8+ recommended)
* **Angular CLI** (if not installed, see instructions below)
* **Python 3.10+** (for backend)
* **pip** (for installing Python dependencies)

## Frontend: Installation and Setup

1. **Clone the repository**

```bash
git clone https://github.com/rocksoncodes/Task-Manager-App.git
cd Frontend-Task-Manager
```

2. **Install Angular CLI** (if not already installed)

```bash
npm install -g @angular/cli
```

3. **Install project dependencies**

```bash
npm install
```

4. **Build the application**

```bash
ng build
```

5. **Run the application locally**

```bash
ng serve
```

6. **Access the app**

Open your browser and go to:

```
http://localhost:4200
```
## Database Setup

The backend API uses **SQLAlchemy** and requires a database to store tasks. By default, it can use **SQLite** for development.

#### 1. Create the database

If using SQLite (simplest for local development):

```bash
# Inside your backend folder
python
>>> from database.database import database_engine
>>> from database.models import Base
>>> Base.metadata.create_all(bind=database_engine)
```
This will create the database file (e.g., tasks.db) and all required tables.

#### 2. Optional: Use another database

You can configure database/database.py to use PostgreSQL, MySQL, or another database by updating the connection URL:
```
# Example for PostgreSQL
DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/taskdb"
```

## Backend: Flask API (Task CRUD)

The backend provides a CRUD API for tasks using Flask and SQLAlchemy. Endpoints are registered under /api/tasks.

## Installation & Setup

1. Navigate to the backend folder:
```
cd Backend-Task-Manager
```

2. Create a virtual environment:
```
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the backend:
```
python app.py
```

5. The API will run on:
```
http://127.0.0.1:5000
```

### Available Endpoints

| Method | Endpoint                                | Description                    | Body / Params                                           |
|--------|----------------------------------------|--------------------------------|--------------------------------------------------------|
| POST   | `/api/tasks/create/task`                | Create a new task              | JSON: `title`, `task_descriptions`, `task_status`, `completed` |
| GET    | `/api/tasks/all`                        | Get all tasks                  | None                                                   |
| GET    | `/api/tasks/<task_status>`              | Get tasks filtered by status   | URL param: `task_status`                               |
| PUT    | `/api/tasks/update/task/<task_id>`      | Update a specific task         | JSON: `title`, `task_descriptions`, `task_status`, `completed` |
| DELETE | `/api/tasks/delete/task/<task_id>`      | Delete a specific task         | URL param: `task_id`                                   |


### Example: Create Task

POST `/api/tasks/create/task`
```
{
  "title": "Finish Report",
  "task_descriptions": "Complete the monthly report",
  "task_status": "pending",
  "completed": false
}
```

## Development Notes

- The app and API are under active development so features may be incomplete or subject to change.
- Contributions and suggestions are welcome. Please fork the repository and submit pull requests.
- If you encounter issues with dependencies, try removing `node_modules` and running `npm install` again.

## Future Features (Planned)

- Add, edit, and delete tasks
- Task prioritization and deadlines
- Responsive design for mobile and desktop
- User authentication and data persistence
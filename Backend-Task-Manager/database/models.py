from sqlalchemy import Column, Integer, Boolean, String
from database import Base, database_engine, session

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(String(30), nullable=False)
    completed = Column(Boolean, nullable=False)


Base.metadata.create_all(database_engine)

new_task = Task(
    title="Test Task",
    description="This is a test task",
    status="pending",
    completed=False
)

if __name__ == "__main__":
    session.add(new_task)
    session.commit()
    task = session.query(Task).first()
    print(task.id, task.title, task.status, task.completed)
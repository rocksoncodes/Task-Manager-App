from sqlalchemy import Column, Integer, Boolean, String
from database.database import Base, database_engine

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    task_descriptions = Column(String(255), nullable=False)
    task_status = Column(String(30), nullable=False)
    completed = Column(Boolean, nullable=False)


Base.metadata.create_all(database_engine)
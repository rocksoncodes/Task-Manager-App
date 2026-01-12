from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

database_engine = create_engine(settings.DB_LINK, echo=True)

Base = declarative_base()


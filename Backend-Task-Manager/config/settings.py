import os
from dotenv import load_dotenv

load_dotenv()

DB_LINK = os.getenv("DATABASE_URL")
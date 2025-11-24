import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'
    # Use SQLite for testing instead of MySQL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///simple_hr_test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
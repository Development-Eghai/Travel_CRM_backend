from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()  # Loads from .env file

class Settings:
    APP_NAME = os.getenv("APP_NAME", "TravelCRM")
    APP_ENV = os.getenv("APP_ENV", "development")
    APP_PORT = int(os.getenv("APP_PORT", 8000))

    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DB = os.getenv("MYSQL_DB")

    SQLALCHEMY_DATABASE_URL = (
        f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )

    print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")  # Debugging line

    # Add other fields as needed...

settings = Settings()
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch values safely
POSTGRES_USER = os.getenv("POSTGRES_USER", "test_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "test@123")
POSTGRES_DB = os.getenv("POSTGRES_DB", "test_db")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"dbname={POSTGRES_DB} user={POSTGRES_USER} password='{POSTGRES_PASSWORD}' host=localhost port={POSTGRES_PORT}"

def get_pg_connection():
    return psycopg2.connect(DATABASE_URL)

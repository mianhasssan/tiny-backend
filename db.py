import os
from dotenv import load_dotenv
import psycopg

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create a database connection
conn = psycopg.connect(DATABASE_URL)

# Create a cursor
cursor = conn.cursor()

# Create tasks table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
)
""")

conn.commit()

# Check whether the table already contains data
cursor.execute("SELECT COUNT(*) FROM tasks")
task_count = cursor.fetchone()[0]

# Seed only once
if task_count == 0:
    example_tasks = [
        ("Learn PostgreSQL", False),
        ("Connect Flask to Docker", False),
        ("Build CRUD API", False)
    ]

    cursor.executemany(
        "INSERT INTO tasks (title, done) VALUES (%s, %s)",
        example_tasks
    )

    conn.commit()
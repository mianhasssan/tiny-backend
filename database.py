import sqlite3

connection = sqlite3.connect("tasks.db")

cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
    )
""")


cursor.execute("SELECT COUNT(*) FROM tasks")
task_count = cursor.fetchone()[0]


if task_count == 0:
    example_tasks = [
        ("Learn SQLite", 0),
        ("Build a Flask API", 0),
        ("Test the API with curl", 0)
    ]

    cursor.executemany(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        example_tasks
    )




connection.commit()


connection.close()

print("Database setup complete.")
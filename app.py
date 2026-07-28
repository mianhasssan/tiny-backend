from flask import Flask, jsonify , request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/tasks", methods=["GET"])
def get_tasks():
    connection = get_db_connection()

    tasks = connection.execute(
        "SELECT * FROM tasks"
    ).fetchall()

    connection.close()

    return jsonify([dict(task) for task in tasks])


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    connection = get_db_connection()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    if task is None:
        return jsonify({
            "error": "Task not found"
        }), 404

    return jsonify(dict(task))

@app.route("/tasks", methods=["POST"])
def create_task():

    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({
            "error": "Title is required"
        }), 400

    title = data["title"].strip()

    if title == "":
        return jsonify({
            "error": "Title is required"
        }), 400

    
    connection = get_db_connection()

 
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (title, 0)
    )

   
    new_id = cursor.lastrowid

    
    connection.commit()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (new_id,)
    ).fetchone()

    connection.close()

    return jsonify(dict(task)), 201



@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.get_json()

    # Validate request body
    if not data or "title" not in data or "done" not in data:
        return jsonify({
            "error": "Title and done are required"
        }), 400

    title = data["title"].strip()
    done = int(bool(data["done"]))

    if title == "":
        return jsonify({
            "error": "Title is required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    # Check if task exists
    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task is None:
        connection.close()
        return jsonify({
            "error": "Task not found"
        }), 404

    # Update task
    cursor.execute(
        """
        UPDATE tasks
        SET title = ?, done = ?
        WHERE id = ?
        """,
        (title, done, task_id)
    )

    connection.commit()

    updated_task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    return jsonify(dict(updated_task))





@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    connection = get_db_connection()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task is None:
        connection.close()
        return jsonify({
            "error": "Task not found"
        }), 404

    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return "", 204







if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify , request
import db

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_tasks():

    db.cursor.execute(
        "SELECT id, title, done FROM tasks ORDER BY id"
    )

    tasks = db.cursor.fetchall()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task[0],
            "title": task[1],
            "done": task[2]
        })

    return jsonify(task_list)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):

    db.cursor.execute(
        "SELECT id, title, done FROM tasks WHERE id = %s",
        (task_id,)
    )

    task = db.cursor.fetchone()

    if task is None:
        return jsonify({
            "error": "Task not found"
        }), 404

    return jsonify({
        "id": task[0],
        "title": task[1],
        "done": task[2]
    })


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

    db.cursor.execute(
        """
        INSERT INTO tasks (title, done)
        VALUES (%s, %s)
        RETURNING id, title, done
        """,
        (title, False)
    )

    new_task = db.cursor.fetchone()
    db.conn.commit()

    return jsonify({
        "id": new_task[0],
        "title": new_task[1],
        "done": new_task[2]
    }), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.get_json()

    if not data or "title" not in data or "done" not in data:
        return jsonify({
            "error": "Title and done are required"
        }), 400

    title = data["title"].strip()
    done = bool(data["done"])

    if title == "":
        return jsonify({
            "error": "Title is required"
        }), 400

    db.cursor.execute(
        """
        UPDATE tasks
        SET title = %s, done = %s
        WHERE id = %s
        RETURNING id, title, done
        """,
        (title, done, task_id)
    )

    updated_task = db.cursor.fetchone()

    if updated_task is None:
        db.conn.rollback()
        return jsonify({
            "error": "Task not found"
        }), 404

    db.conn.commit()

    return jsonify({
        "id": updated_task[0],
        "title": updated_task[1],
        "done": updated_task[2]
    })




@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    db.cursor.execute(
        """
        DELETE FROM tasks
        WHERE id = %s
        RETURNING id
        """,
        (task_id,)
    )

    deleted_task = db.cursor.fetchone()

    if deleted_task is None:
        db.conn.rollback()
        return jsonify({
            "error": "Task not found"
        }), 404

    db.conn.commit()

    return "", 204





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
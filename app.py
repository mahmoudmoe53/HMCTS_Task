from flask import Flask, request, jsonify, send_from_directory
from HMCTS_Task.database import TaskDB

app = Flask(__name__, static_folder="frontend", static_url_path="")

db = TaskDB()



@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("frontend", filename)



@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "title is required"}), 400

    task_id = db.create_task(
        title=data["title"].strip(),
        description=data.get("description"),
        status=data.get("status", "todo"),
        due_date=data.get("due_date")
    )
    return jsonify({"id": task_id}), 201



@app.route("/api/tasks", methods=["GET"])
def get_all_tasks():
    tasks = db.get_all_tasks()
    return jsonify([
        {
            "id": t[0],
            "title": t[1],
            "description": t[2],
            "status": t[3],
            "due_date": t[4].isoformat() if t[4] else None
        } for t in tasks
    ])


@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    t = db.get_task(task_id)
    if not t:
        return jsonify({"error": "not found"}), 404
    return jsonify({
        "id": t[0],
        "title": t[1],
        "description": t[2],
        "status": t[3],
        "due_date": t[4].isoformat() if t[4] else None
    })



@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    data = request.get_json()
    if not data or "status" not in data:
        return jsonify({"error": "status is required"}), 400

    updated = db.update_task_status(task_id, data["status"])
    if not updated:
        return jsonify({"error": "not found"}), 404

    return jsonify({"id": updated[0], "status": data["status"]})


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted = db.delete_task(task_id)
    if not deleted:
        return jsonify({"error": "not found"}), 404
    return "", 204



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []


@app.route("/task", methods=["POST"])
def add_task():
    data = request.get_json()

    task = {
        "title": data.get("title"),
        "status": data.get("status")
    }

    tasks.append(task)

    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


if __name__ == "__main__":
    app.run(debug=True)
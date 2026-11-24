from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Vinay"},
    {"id": 2, "name": "Uday"}
]


@app.route("/students")
def get_students():
    return jsonify({
        "success": True,
        "message": "Students found",
        "data": students
    })


@app.route("/student/<int:id>")
def get_student(id):

    for student in students:
        if student["id"] == id:
            return jsonify({
                "success": True,
                "message": "Student found",
                "data": student
            })

    return jsonify({
        "success": False,
        "message": "Student not found",
        "data": None
    }), 404


if __name__ == "__main__":
    app.run(debug=True)

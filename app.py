from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Default student data
students = [
    {"id": 1, "name": "Rahul", "roll": "101", "dept": "CSE"},
    {"id": 2, "name": "Anita", "roll": "102", "dept": "ECE"},
    {"id": 3, "name": "Karan", "roll": "103", "dept": "ME"},
    {"id": 4, "name": "Sneha", "roll": "104", "dept": "IT"},
    {"id": 5, "name": "Aman", "roll": "105", "dept": "CSE"}
]

@app.route("/")
def home():
    return render_template("index.html")

# READ
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# CREATE
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    new_id = students[-1]["id"] + 1 if students else 1
    student = {
        "id": new_id,
        "name": data.get("name"),
        "roll": data.get("roll"),
        "dept": data.get("dept")
    }
    students.append(student)
    return jsonify({"message": "Student added"})

# UPDATE
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    for s in students:
        if s["id"] == id:
            s["name"] = data.get("name")
            s["roll"] = data.get("roll")
            s["dept"] = data.get("dept")
            return jsonify({"message": "Student updated"})
    return jsonify({"error": "Student not found"}), 404

# DELETE
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


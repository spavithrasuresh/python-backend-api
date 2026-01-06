from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    users.append(data)
    return {"message": "User added successfully"}, 201

if __name__ == "__main__":
    app.run(debug=True)

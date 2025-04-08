from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if data["username"] in users:
        return jsonify({"error": "User already exists"}), 400
    users[data["username"]] = data["password"]
    return jsonify({"message": "User registered successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if users.get(data["username"]) == data["password"]:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)

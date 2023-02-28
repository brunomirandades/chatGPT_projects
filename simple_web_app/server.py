from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/add", methods=["POST"])
def add_user():
    user_data = request.get_json()
    user_id = user_data.get("id")
    name = user_data.get("name")
    age = user_data.get("age")
    address = user_data.get("address")
    with open("user_data.txt", "a") as f:
        f.write(f"{user_id},{name},{age},{address}\n")
    return "User added successfully"


@app.route("/get", methods=["GET"])
def get_user():
    user_id = request.args.get("id")
    with open("user_data.txt", "r") as f:
        for line in f:
            if line.startswith(user_id + ","):
                user_data = line.strip().split(",")
                return {
                    "id": user_data[0],
                    "name": user_data[1],
                    "age": user_data[2],
                    "address": user_data[3],
                }
    return "User not found"

if __name__ == "__main__":
    app.run()

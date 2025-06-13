from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Fernet Encryptor is running!"

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    key = data.get("key")
    payload = data.get("data")

    if not key or not payload:
        return jsonify({"error": "Missing key or data"}), 400

    try:
        fernet = Fernet(key.encode())
        token = fernet.encrypt(payload.encode()).decode()
        return jsonify({"token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()

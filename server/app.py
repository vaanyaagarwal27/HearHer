from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify({"message": "HearHer API is running"})

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "service": "hearher"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
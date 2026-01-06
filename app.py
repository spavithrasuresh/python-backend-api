from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Python Backend API is running successfully 🚀"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "OK",
        "message": "Backend is healthy 💚"
    })

if __name__ == "__main__":
    app.run(debug=True)

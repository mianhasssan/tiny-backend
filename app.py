from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
        return jsonify(
            {
        "status": "success",
        "message": "Welcome to my Tiny Backend API"
            })

@app.route("/hello")
def hello():
        return jsonify({
        "message": "Hello, World!"
    })

if __name__ == "__main__":
    app.run(debug=True)
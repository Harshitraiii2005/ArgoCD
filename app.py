from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Go to /hello?name=YourName"

@app.route("/hello")
def hello():
    name = request.args.get("name", "Friend")
    return f"Hello {name}, how are you? I hope you're good."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

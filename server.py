from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()

    user = data.get("user", "unknown")
    timestamp = data.get("timestamp", str(datetime.datetime.now()))
    keys = data.get("keys", [])

    print(f"[{timestamp}] ({user}) -> {keys}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

from flask import Flask, request
import datetime
import logging

app = Flask(__name__)

# Enable debug mode for better logging
app.debug = True

# Set up logging to display in the console
logging.basicConfig(level=logging.DEBUG)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()

    # Debugging to check the received data
    app.logger.debug(f"Received Data: {data}")  # Detailed log for received data

    user = data.get("user", "unknown")
    timestamp = data.get("timestamp", str(datetime.datetime.now()))
    keys = data.get("keys", [])

    app.logger.debug(f"[{timestamp}] ({user}) -> {keys}")  # Detailed log for keys
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

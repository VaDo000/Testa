from flask import Flask, request
import datetime
import logging

app = Flask(__name__)

# Enable debug mode for better logging
app.debug = True

# Set up logging to display in the console
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')

# Suppress werkzeug logs by setting its log level to WARNING
logging.getLogger('werkzeug').setLevel(logging.WARNING)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()

    user = data.get("user", "unknown")
    timestamp = data.get("timestamp", str(datetime.datetime.now()))
    keys = data.get("keys", [])

    # Log the desired debug message in your required format
    app.logger.debug(f"[{timestamp}] ({user}) -> {keys}")

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

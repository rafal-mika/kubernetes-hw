from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def hello_from_api():
    random_status = randint(0, 1)
    response = "<p> Hello from API !!!</p>"
    return response if random_status else 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

from flask import Flask

app = Flask(__name__)


@app.route("/api2")
def hello_world_from_api():
    return "<p> Hello World from API 2 !!!</p>"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

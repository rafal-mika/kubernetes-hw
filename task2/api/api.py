from flask import Flask
import psycopg2
import os

app = Flask(__name__)

conn_string = os.getenv("CONNECTION_STRING")


def connect_to_db(conn_str):
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    return conn


@app.route("/is-db-connected")
def is_db_connected():
    with connect_to_db(conn_string) as connection:
        return "<p>Connection is up</p>" if not connection.closed else "<p>Connection is down</p>"

@app.route("/")
def hello_world():
    return "<p> Hellow World ! </p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

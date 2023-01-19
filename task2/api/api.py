from flask import Flask
import psycopg2
import os

app = Flask(__name__)

connection_string = os.getenv("POSTGRES_CONNECTION_STRING")


def connect_to_db(conn_str):
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    return conn


@app.route("/")
def hello_world():
    return "<p> Hello World !</p>"


@app.route("/db-version")
def get_db_version():
    with connect_to_db(connection_string) as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT version()')
            version = cursor.fetchall()
            return {"database":version[0][0]}


@app.route("/is-db-connected")
def get_db_connection_status():
    with connect_to_db(connection_string) as connection:
        status = "Connection is up" if not connection.closed else "Connection is down"
        return {"connection status":status}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

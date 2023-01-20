from flask import Flask
from urllib.request import urlopen
from urllib.error import HTTPError
from retrying import retry

app = Flask(__name__)


@app.route("/")
def get_request_from_other_api():
    try:
        return get_request_from_api2()
    except HTTPError as error:
        if error.code == 500:
            return "<p>Service temporary unavailable. Please try later...<p>"
        else:
            raise


@retry(wait_exponential_multiplier=1000, wait_exponential_max=8000,
       stop_max_attempt_number=5)
def get_request_from_api2():
    return urlopen("http://api2").read()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

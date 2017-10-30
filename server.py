import json
import oauth2 as oauth
from secret import keys 
from flask import (Flask, jsonify)


app = Flask(__name__)
app.secret_key = "miau"


def authorize():
    """authorize w/ twitter api and fetch recent codenewbie tweets, return a json"""

    consumer = oauth.Consumer(key=keys["consumer_key"], secret=keys["consumer_secret"])
    access_token = oauth.Token(key=keys["access_token"], secret=keys["access_secret"])
    client = oauth.Client(consumer, access_token)

    test_url = "https://api.twitter.com/1.1/search/tweets.json?q=codenewbie&result_type=recent"
    response, data = client.request(test_url)

    return  json.loads(data)


if __name__ == "__main__":
    app.run()

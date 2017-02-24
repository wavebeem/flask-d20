"""
Just an app!
I don't know what you want, pylint!
"""

from random import randint
from flask import Flask, jsonify

# Have to call it `application` for Elastic Beanstalk to work? lol
application = Flask(__name__)

@application.route('/')
def index():
    """Here's the index function!"""
    number = randint(1, 20)
    is_critical = number == 20
    is_failure = number == 1
    return jsonify({
        'number': number,
        'is_critical': is_critical,
        'is_failure': is_failure
    })

if __name__ == '__main__':
    application.run()

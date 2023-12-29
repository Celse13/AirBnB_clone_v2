#!/usr/bin/python3
"""Running the flask for my web application
    listening on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def dsiplay_states_list():
    """Displaying state id and name"""
    states_cls = storage.all('State').values()
    return render_template('7-states_list.html', states=states_cls)


@app.teardown_appcontext
def teardown():
    """Close session when app content torn down."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

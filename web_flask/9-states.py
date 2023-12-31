#!/usr/bin/python3
"""Running the flask for my web application
    listening on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def the_states(id=None):
    """List states"""
    states = retrieve_state_by_id(id)
    return render_template('9-states.html', states=states, state_id=id)


def retrieve_state_by_id(state_id):
    """Retrieve state by state_id"""
    states = storage.all(State)
    if state_id:
        key = "{}.{}".format(State.__name__, state_id)
        states = states.get(key, None)
    else:
        states = states.values()
    return states


@app.teardown_appcontext
def close(arg=None):
    """Close session when app conten torn down."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

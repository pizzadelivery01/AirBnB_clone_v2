#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_all_states():
    """
    all states
    """
    all_states = storage.all(State).values()
    return render_template('9-states.html', all_states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def find_state(id=None):
    """
    state wit id
    """
    dict_states = storage.all(State)
    all_states = []
    all_states_id = []
    for k, v in dict_states.items():
        all_states_id.append(v.id)
        all_states.append(v)
        return render_template('9-states.html', all_states=all_states,
                               all_states_id=all_states_id, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """
    teardown
    """
    storage.close()

if __name__ == '__main__':
    app.run()

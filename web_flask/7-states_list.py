#!/usr/bin/python3
"""Flask"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    states_list
    """
    states_list = []
    storage.reload()

    for v in storage.all("State").values():
        states_list.append([v.id, v.name])

    return render_template("7-states_list.html", states=states_list)


@app.teardown_appcontext
def teardown_db(exception):
    """
    teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run()

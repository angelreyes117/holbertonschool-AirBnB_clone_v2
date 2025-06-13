#!/usr/bin/python3
""" Flask app that lists states """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page with list of states"""
    states = storage.all(State)
    states_sorted = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_sorted)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

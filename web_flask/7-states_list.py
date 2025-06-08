#!/usr/bin/python3
"""
Task 7: /states_list – display all State objects
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    states.sort(key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


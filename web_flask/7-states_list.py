#!/usr/bin/python3
''' Flask web application '''

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def state_list():
    # Get all State objects as a dictionary, convert to list, and sort by name
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=all_states)

@app.teardown_appcontext
def teardown_appcontext(self):
    # Close the storage session after each request
    return storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

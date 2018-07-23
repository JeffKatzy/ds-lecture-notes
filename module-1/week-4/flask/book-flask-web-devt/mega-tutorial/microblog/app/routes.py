from app import app
from flask import render_template

@app.route('/')
def index():
    users = [{'name': 'bob'}, {'name': 'fred'}]
    return render_template('index.html', users=users)

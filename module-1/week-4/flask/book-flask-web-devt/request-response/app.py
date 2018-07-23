from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import pdb
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


db.init_app(app)
@app.route('/')
def index():
    # response = app.make_response(('whatever', 204))
    r = json.dumps({'foo': 'bar'})
    return r, 200, {'content-type': 'application/json'}

def show(name):
    return

# app.add_url_rule('/', 'index', index)

# app.run(debug=True)
# what's impo

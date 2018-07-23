import pdb
from flask import Flask
from flask import request, make_response

app = Flask(__name__)

    # the name argument - is used to determine the root path of the application
    # so that it can later find files relative to the location of the app

# @app.route('/')

def index():
    response = make_response('here is some stuff', 200)
    return response

app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
    app.run(debug=True)

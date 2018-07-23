from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import dash_core_components as dcc
import dash_html_components as html

import pdb
import dash
# print(__name__, 'from package.py')

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///moes.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(server)
migrate = Migrate(server, db)
from package.models import *

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard')

from package.dashboard import app
import package.routes

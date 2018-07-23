from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import pdb
from flask_migrate import Migrate
# print(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///espn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    city = db.Column(db.String(100), unique=True)

@app.route('/nba/teams')
def index():
    teams = Team.query.all()
    return render_template('index.html', teams = teams)

@app.route('/nba/teams/<id>')
def show(id):
    team = Team.query.get(id)
    return render_template('show.html', team_name=team.name)


# flask db init
# flask db migrate -m "users table"
#

# if __name__ == '__main__':
#     app.run(debug=True)

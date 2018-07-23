from flask import Blueprint, render_template
from bookshelf.data.models import Author
users = Blueprint('users', __name__, template_folder='templates')

@users.route('/')
def index():
    authors = Author.query.all()

    return render_template('index.html', authors=authors)

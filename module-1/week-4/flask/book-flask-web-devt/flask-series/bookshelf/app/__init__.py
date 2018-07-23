from flask import Flask
from bookshelf.database import db
from bookshelf.users.controllers import users
from bookshelf.main.controllers import main
from bookshelf.data.models import Author, Book
from flask.ext.migrate import Migrate, MigrateCommand

def create_app():
    app = Flask(__name__)
    app.config.from_object('bookshelf.config.DevelopmentConfig')
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(main, url_prefix='/')
    import bookshelf.data.models
    db.init_app(app)
    return app

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Author=Author)

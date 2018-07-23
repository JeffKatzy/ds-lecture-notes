from bookshelf import app
from bookshelf.data.models import db

# from flask.ext.script import Shell, Manager

# def make_shell_context():
#     return dict(app=app, db=db, Author=Author)

# manager = Manager(create_app)
# manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == '__main__':
    app.run()

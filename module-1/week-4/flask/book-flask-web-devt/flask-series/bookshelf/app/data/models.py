from bookshelf.database import db


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return '<Author %r>' % (self.name)

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    rating = db.Column(db.Integer)
    image = db.Column(db.String(30))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship('Author',
                             backref=db.backref('books', lazy='joined'))

    def __repr__(self):
        return '<Book %r>' % (self.title)

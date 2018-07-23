from books_management import db


class Publisher(db.Model):
    isbn = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, isbn, name):
        self.isbn = isbn
        self.name = name

    def __repr__(self):
        return '<Publisher %r %s>' % (self.isbn, self.name)
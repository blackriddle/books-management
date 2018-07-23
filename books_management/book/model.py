from books_management import db


class Book(db.Model):
    book_id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    barcode = db.Column(db.INTEGER, nullable=False)

    def __init__(self, book_id, barcode):
        self.book_id = book_id
        self.barcode = barcode

    def __repr__(self):
        return '<Book %s %s>' % (self.book_id, self.barcode)

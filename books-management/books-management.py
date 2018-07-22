import os

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

basedir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Publisher=Publisher, Book=Book)


class Publisher(db.Model):
    isbn = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, isbn, name):
        self.isbn = isbn
        self.name = name

    def __repr__(self):
        return '<Publisher %r %s>' % (self.isbn, self.name)


class Book(db.Model):
    book_id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    barcode = db.Column(db.INTEGER, nullable=False)

    def __init__(self, book_id, barcode):
        self.book_id = book_id
        self.barcode = barcode

    def __repr__(self):
        return '<Book %s %s>' % (self.book_id, self.barcode)


@app.route('/')
def show_all():
    return render_template('main.html')


@app.route('/book/')
def show_all_books():
    return render_template('show_all_books.html',
                           books=Book.query.order_by(Book.id).asc().all()
                           )


@app.route('/book/add/', methods=['POST'])
def add_a_book():
    if request.method == 'POST':
        book_id = request.form.get['book_id', '']
        barcode = request.form.get['barcode', '']
        if not book_id:
            flash('Book-ID is required', 'error')
        elif not barcode:
            flash('Barcode is required', 'error')
        else:
            book = Book(book_id=book_id, barcode=barcode)
            db.session.add(book)
            db.session.commit()
            flash(u'Book item is successfully created.')
            return redirect(url_for('show_all_books'))
    return render_template('add_a_book.html')


@app.route('/book/del/', methods=['POST'])
def del_a_book():
    if request.method == 'POST':
        book_id = request.form.get['book_id', '']
        if not book_id:
            flash('Book-ID is required', 'error')
        else:
            book = Book.query.filter(Book.book_id == book_id).first()
            db.session.delete(book)
            db.session.commit()
            flash(u'Book item is successfuuly deleted.')
            return redirect(url_for('show_all_books'))
    return render_template('del_a_book.html')


@app.route('/book/update/', methods=['POST'])
def update_a_book():
    if request.method == 'POST':
        book_id = request.form.get['book_id', '']
        barcode = request.form.get['barcode', '']
        if not book_id:
            flash('Book-ID is required', 'error')
        else:
            book = Book.query.filter(Book.book_id == book_id).first()
            book.barcode = barcode
            db.session.commit()
            flash(u'Book item is successfully updated.')
            return redirect(url_for('show_all_books'))
    return render_template('update_a_book.html')


@app.route('/book/query/', methods=['GET', 'POST'])
def query_book():
    if request.method == 'POST' or request.method == 'GET':
        book_id = request.form.get['book_id', '']
        barcode = request.form.get['barcode', '']
        books = Book.query.filter(Book.book_id == book_id, Book.barcode == barcode).asc().all()
        return render_template('show_all_books.html',
                               books=books)


@app.route('/publisher/')
def show_publisher():
    pass


@app.route('/publisher/add/')
def add_publisher():
    pass


@app.route('/publisher/del/')
def del_publisher():
    pass


@app.route('/publisher/update/')
def update_publisher():
    pass


@app.route('/publisher/query/')
def query_publisher():
    pass


if __name__ == '__main__':
    manager.run()

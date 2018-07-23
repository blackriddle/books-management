from flask import flash, render_template
from flask_restful import Resource

from books_management import db
from model import Book


class BookResource(Resource):
    def get(self, book_id='', barcode=''):
        if not book_id:
            return render_template('show_books.html',
                                   books=Book.query.order_by(Book.id).asc().all()
                                   )
        books = Book.query.filter(Book.book_id == book_id,
                                  Book.barcode == barcode).asc().all()
        return render_template('show_books.html',
                               books=books)

    def post(self, book_id='', barcode=''):
        if not book_id:
            flash('Book-ID is required', 'error')
        elif not barcode:
            flash('Barcode is required', 'error')
        else:
            book = Book(book_id=book_id, barcode=barcode)
            db.session.add(book)
            db.session.commit()
            flash(u'Book item is successfully created.')
            return render_template('show_books.html',
                                   books=Book.query.order_by(Book.id).asc().all()
                                   )

    def patch(self, book_id='', barcode=''):
        if not book_id:
            flash('Book-ID is required', 'error')
        else:
            book = Book.query.filter(Book.book_id == book_id).first()
            book.barcode = barcode
            db.session.commit()
            flash(u'Book item is successfully updated.')
            return render_template('show_books.html',
                                   books=book
                                   )

    def delete(self, book_id='', barcode=''):
        if not book_id:
            flash('Book-ID is required', 'error')
        else:
            book = Book.query.filter(Book.book_id == book_id).first()
            db.session.delete(book)
            db.session.commit()
            flash(u'Book item is successfuuly deleted.')
            return render_template('show_books.html',
                                   books=Book.query.order_by(Book.id).asc().all()
                                   )

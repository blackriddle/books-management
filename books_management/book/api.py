from books_management import api
from resource import BookResource

api.add_resource(BookResource, '/book/', '/book/<book_id>')

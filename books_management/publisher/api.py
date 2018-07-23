from books_management import api
from resource import PublisherResource

api.add_resource(PublisherResource, '/publisher/', '/publisher/<isbn>')

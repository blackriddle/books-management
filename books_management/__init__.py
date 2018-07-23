import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask('books_management')

basedir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
api = Api(app)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class App(object):
    def __init__(self, name):
        self.app = Flask(name)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = None
        self.app.config['SECRET KEY'] = 'For the glory of kwnkwcnwkcdmnsvedv25441fefvegf'
        self.db = None

    def run(self):
        self.app.run(debug=True)

    def run_db(self, password):
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{password}@localhost/fuel_db'
        self.db = SQLAlchemy(self.app)



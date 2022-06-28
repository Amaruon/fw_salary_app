from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class App(object):
    def __init__(self, name, password):
        self.app = Flask(name)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{password}@localhost/fuel_db'
        self.db = SQLAlchemy(self.app)

    def run(self):
        self.app.run()

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:1podnano&@localhost/fuel_db'
    app.config['SECRET KEY'] = 'For the glory of kwnkwcnwkcdmnsvedv25441fefvegf'

    @app.route('/')
    def home():
        return render_template('home_page.html')

    return app
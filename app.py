from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
oauth = OAuth2Provider(app)

from app import db
from routes import *

from models import Item

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print(Item.query.all())
    app.run(debug=True)
    
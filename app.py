from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
oauth = OAuth2Provider(app)

from routers.item_router import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

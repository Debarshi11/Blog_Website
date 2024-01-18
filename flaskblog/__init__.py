from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = '02674151deb9c5902e15bdd855ee11b5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
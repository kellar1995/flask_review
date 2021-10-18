from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'randomstring'

from app import routes
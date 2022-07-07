import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    res = db.engine.execute("SELECT 1").scalar()
    return f"<p>Hello, {res}!</p>"

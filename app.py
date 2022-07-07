import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    sql = "SELECT * FROM patients"
    res = db.engine.execute(sql)

    head = "<tr><th>ID</td><th>Фамилия</th><th>Имя</th></tr>"
    row_tpl = "<tr><td>{patient_id}</td><td>{patient_last_name}</td><td>{patient_first_name}</td></tr>"
    rows = [row_tpl.format(**r) for r in res]
    body = "".join(rows)
    table = f"<table><thead>{head}</thead><tbody>{body}</tbody></table>"

    return table

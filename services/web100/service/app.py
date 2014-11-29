#!/usr/bin/python

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
import json
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
THE_FLAG = open('flag').read().strip()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(256), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Secret(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True)
    value = db.Column(db.String(128), unique=True)

    def __init__(self, key, value):
        self.key = key
        self.value = value


DEFAULT_CONTACTS = json.loads(open("contacts.json").read())

def db_reset():
    db.drop_all()
    db.create_all()
    for (name, email) in DEFAULT_CONTACTS:
        db.session.add(Contact(name, email))
        #db.session.add(Secret('%s_secret' % (name), email[::-1]))
    db.session.add(Secret('flag', THE_FLAG))
    db.session.commit()


@app.route('/', methods=["GET", "POST"])
def home():
    db_reset()
    if request.method == "POST" and "name" in request.form:
        return redirect("/%s" % (request.form["name"]))
    contacts = [c.name for c in Contact.query.all()]
    return render_template("index.html", contacts=contacts)


@app.route('/<name>')
def hello_name(name):
    db_reset()
    contact = Contact.query.filter("name='%s'" % (name)).first()
    email = None
    if contact:
        email = contact.email

    return render_template("contact.html", name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

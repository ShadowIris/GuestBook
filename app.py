import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import SignupForm

from models import Signups
from database import db_session

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        signup = Signups(name=form.name.data, email=form.email.data, date_signed_up=datetime.datetime.now())
        db_session.add(signup)
        db_session.commit()
        records = Signups.query.all()
        return render_template('record.html', records = records)
    return render_template('signup.html', form=form)

@app.route("/success", methods=('GET', 'POST'))
def success():
    records = Signups.query.all()
    return render_template('record.html', records = records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)

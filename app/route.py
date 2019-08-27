from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { "username": "MuteBisthop"}
    posts = [
        {
            "author": {"username" : "John"},
            "body": "Starter template Be sure to have your pages set up with the latest design and development standards. \
            That means using an HTML5 doctype and including a viewport meta tag for proper responsive behaviors. \
            Put it all together and your pages should look like this"
        },
        {
            "author": {"username" : "Jonny"},
            "body": "Starter template Be sure to have your pages set up with the latest design and development standards. \
            That means using an HTML5 doctype and including a viewport meta tag for proper responsive behaviors. \
            Put it all together and your pages should look like this"
        },
        ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user "{form.username.data}"')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
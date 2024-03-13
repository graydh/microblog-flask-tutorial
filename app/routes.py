from flask import render_template, flash, redirect, url_for

from app import app

from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successfully requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Declan'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Amherst!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Oppenheimer summer 2023!'
        }
    ]

    return render_template('index.html', title="Home page", user=user, posts=posts)
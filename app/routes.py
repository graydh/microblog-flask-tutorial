from flask import render_template

from app import app

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
from flask import render_template, flash, redirect, url_for
from app import app
import datetime
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    time_act = datetime.datetime.now()

    questions = [
        {
            'What is love?': 'I dont know.',
            'Who is it?': 'Michael Jackson',
            'Where is the gold?': 'Under the Rainbow',
            'How is the weather?': 'Its sunny.'
        }
    ]

    return render_template('index.html', title="Online-Quizsystem", questions=questions, time=time_act)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

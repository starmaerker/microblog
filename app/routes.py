from flask import render_template, flash, redirect, url_for
from app import app
import datetime
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User


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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filer_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

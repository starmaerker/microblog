from flask import render_template
from app import app
import datetime


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

    return render_template('index.html', questions=questions, time=time_act)

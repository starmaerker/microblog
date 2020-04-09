from flask import render_template
from app import app
import time


@app.route('/')
@app.route('/index')
def index():
    time_act = time.time()

    return render_template('index.html', title='Online-Quizsystem', time=time_act)
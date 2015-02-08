from dasher import *
import models

import sqlite3
from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash

@app.route('/')
def render_splash_page():
    return render_template('index.html')

@app.route('/home')
def render_home_page():
    users = db.session.query(models.User).all()
    return render_template('home.html', users=users)

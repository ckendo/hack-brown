from dasher import *
import models

import sqlite3
from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash

@app.route('/')
def main():
    users = db.session.query(models.User).all()
    interests = db.session.query(models.Interest).all()
    all_text = ["<li>%s</li>" % str(user) for user in users]
    all_text += ["<li>%s</li>" % str(interest) for interest in interests]

    # FIXME Put this in a real templating engine
    return "<ul>%s</ul>" % "".join(all_text)

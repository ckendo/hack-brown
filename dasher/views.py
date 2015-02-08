from dasher import *
import models

import sqlite3
from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash

@app.route('/')
def main():
    users = db.session.query(models.User).all()
    all_text = ["%s %s" % (user.name, user.description) for user in users]

    return " | ".join(all_text)

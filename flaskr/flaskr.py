# all the imports
import os
from peewee import *
from flaskr.connectdatabase import ConnectDatabase
from flaskr.models import UserStories
from flaskr.build import Builder
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app


app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def init_db():
    ConnectDatabase.db.connect()
    ConnectDatabase.db.create_tables([UserStories], safe=True)


def create_data():
    rowsnum = UserStories.select().count()
    if rowsnum == 0:
        build = Builder()
        build.create_dummy_data()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.cli.command('createdata')
def createdata_command():
    """Adds the user stories to the table"""
    create_data()
    print('The user stories from the csv file have been added to the table.')


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()


@app.route('/')
def show_entries():
    entries = UserStories.select().order_by(UserStories.id.desc())
    return render_template('list.html', entries=entries)


@app.route('/story', methods=['POST'])
def add_entry():
    new_entry = UserStories.create(story_title=request.form['story_title'], user_story=request.form['user_story'], acceptance_criteria=request.form['acceptance_criteria'], business_value=request.form['business_value'], estimation=request.form['estimation'])
    new_entry.save()
    flash('New user story was successfully created')
    return redirect(url_for('list'))
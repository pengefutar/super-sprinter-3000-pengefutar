from flaskr.connectdatabase import ConnectDatabase
from peewee import *


class UserStories(Model):
    story_title = TextField()
    user_story = TextField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = IntegerField()
    status = CharField()

    class Meta:
        database = ConnectDatabase.db
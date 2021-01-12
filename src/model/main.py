from mongoengine import *

class Song():
    title = StringField()
    id = StringField()
    link = StringField()
    avatar = StringField()
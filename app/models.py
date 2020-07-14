from flask import current_app
from mongoengine import Document, StringField, EmailField, BooleanField



class User(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    otp = StringField(required=True)
    conf = BooleanField(default=False)
from flask_wtf import FlaskForm
from wtforms import *


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    name = StringField('Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Passwords must match')
    ])
    password_confirm = PasswordField('Repeat Password')
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required


class ProfileUpdate(FlaskForm):
    username = StringField('username', validators=[data_required()])
    name = StringField('name', validators=[data_required()])
    email = StringField('email', validators=[data_required()])
    password = StringField('password', validators=[data_required()])
    submit = SubmitField('submit')

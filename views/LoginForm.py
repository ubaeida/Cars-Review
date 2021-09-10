from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required


class LoginForm(FlaskForm):
    username = StringField('username', validators=[data_required()])
    password = StringField('password', validators=[data_required()])
    submit = SubmitField('submit')

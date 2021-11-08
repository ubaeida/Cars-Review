from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required


class SearchForm(FlaskForm):
    car_make = StringField('car_make', validators=[data_required()])
    car_model = StringField('car_model', validators=[data_required()])
    year = StringField('year', validators=[data_required()])
    submit = SubmitField('submit')

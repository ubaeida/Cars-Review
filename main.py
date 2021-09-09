# Cars review project.
# 1-  Register a user
# 2- log in
# 3- show cars from database
# 4- add and edit cars to the database
# 5- View cars details (show for everyone)
# 6- add car review  and opinion box
# 7- search for cars
# 8- log out

#############################
# init User
# init car
# init review

#############################
# database.
# table for users (id, username, password)
# table for cars (id , car name, car model, year, image)
# table for review (car_id, id_user, opinion box, rate of 10)

from flask import *
from flask_session import Session

from servcies import user_service
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required
import os
from servcies import car_service

user_service = user_service.UserService()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route("/")
def hello_world():
    cars = car_service.CarService().show_cars()
    return render_template("index.html", title="Welcome to show cars app", cars=cars)


@app.route('/<car_id>', methods=['GET', 'POST'])
def car_details(car_id):
    if request.method == 'POST':
        review = request.form.get('review')
        user_id = session['ID']
        user_service.add_review(user_id, car_id, review)
    car, reviews = car_service.CarService().get_car_details1(car_id)
    return render_template('car_details.html', title='Car details', car=car, reviews=reviews)


@app.route("/post_review", methods=['POST'])
def post_review():
    car_id = request.form.get('car_id')
    review = request.form.get('review')
    user_id = session['ID']
    user_service.add_review(car_id, user_id, review)
    return redirect(url_for('car_details', car_id=car_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[data_required()])
    password = StringField('password', validators=[data_required()])
    submit = SubmitField('submit')


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form, title="Log in")


@app.route("/do_login", methods=['POST'])
def do_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    service_out = user_service.user_log_in(username, password)
    if service_out is None:
        flash('error login in')
        er = "user name not found"
        return render_template('login.html', form=form, er=er)
    else:
        session['ID'] = service_out.myid
        return redirect(url_for('hello_world'))


@app.route('/logout')
def ses_end():
    session.pop('ID', None)
    return redirect(url_for('login'))


@app.route("/register")
def register():
    form = LoginForm()
    return render_template("register.html", form=form, title="Registration")


@app.route("/do_register", methods=['POST'])
def do_register():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    user_service.register_user(username, password)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)

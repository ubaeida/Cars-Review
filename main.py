import os
from flask import *
from flask_session import Session
from servcies.car_service import CarService
from servcies.user_service import UserService
from views.LoginForm import LoginForm
from views.RegisterForm import RegisterForm

user_service = UserService()
car_service = CarService()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route("/")
def index():
    cars = car_service.show_cars()
    return render_template("index.html", title="Welcome to show cars app", cars=cars)


@app.route('/<car_id>', methods=['GET', 'POST'])
def car_details(car_id):
    if request.method == 'POST':
        review = request.form.get('review')
        user_id = session['ID']
        user_service.add_review(user_id, car_id, review)
    car, reviews = car_service.get_car_details(car_id)
    imges = car_service.get_car_img(car_id)
    return render_template('car_details.html', title='Car details', car=car, reviews=reviews, img=imges)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        service_out = user_service.user_log_in(username, password)
        if service_out is None:
            flash('error login in')
            er = "user name not found"
            return render_template('login-v2.html', form=form, er=er)
        else:
            session['ID'] = service_out.myid
            return redirect(url_for('index'))
    return render_template("login-v2.html", form=form, title="Log in")


@app.route('/logout')
def ses_end():
    session.pop('ID', None)
    return redirect(url_for('index'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        name = form.name.data
        email = form.email.data
        user_service.register_user(username, password, name, email)
        return redirect(url_for('login'))
    return render_template("register-v2.html", form=form, title="Registration")


if __name__ == "__main__":
    app.run(debug=True)

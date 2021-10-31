import os
from flask import *
from flask_session import Session
from servcies.car_service import CarService
from servcies.user_service import UserService
from servcies.ReviewService import ReviewService
from views.LoginForm import LoginForm
from views.ProfileUpdate import ProfileUpdate
from views.RegisterForm import RegisterForm
from servcies.attribute_service import AttributeService
from flask_admin import Admin


user_service = UserService()
car_service = CarService()
ReviewService = ReviewService()
AttributeService = AttributeService()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='microblog', template_mode='bootstrap3')

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
        all_review = request.form.get('all_review')
        engine_review = request.form.get('engine_review')
        comfort_review = request.form.get('comfort_review')
        fuel_review = request.form.get('fuel_review')
        stability_review = request.form.get('stability_review')
        safety_review = request.form.get('safety_review')
        technology_review = request.form.get('technology_review')
        user_comment = request.form.get('user_comment')
        user_id = session['ID']
        ReviewService.add_review(user_id, car_id, all_review, engine_review, comfort_review, fuel_review,
                                 stability_review, safety_review, technology_review, user_comment)
    car, all_review = car_service.get_car_details(car_id)
    gallery = car_service.get_car_img(car_id)
    car_attributes = AttributeService.get_attributes(car_id)
    return render_template('car_details.html', title='Car details', car=car, gallery=gallery, all_review=all_review,
                           car_attributes=car_attributes)


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


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session['ID']
    users = user_service.user_profile(user_id)
    user_activities = user_service.user_activity(user_id)
    form = ProfileUpdate()
    if request.method == 'post':
        username = request.form.get('username')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user_service.update_profile(username, name, password, email, user_id)

    return render_template("profile.html", user=user, user_activities=user_activities, form=form)


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

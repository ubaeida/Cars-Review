from mysql.connector import (connection)
from models.Car import Car
from models.Review import Review


db = connection.MySQLConnection(user='root', password='newpass',
                              host='127.0.0.1',
                              database='cars')

class CarService:

    def show_cars(self):
        c = db.cursor()
        c.execute("select * from cars")
        rows = c.fetchall()
        # imperative style
        # cars = []
        # for row in rows:
        #    cars.append(Car(row[0], row[1], row[2], row[3], row[4]))

        # functional style
        return map(lambda row: Car(row[0], row[1], row[2], row[3], row[4]), rows)

    def get_car_details(self, car_id):
        c = db.cursor()
        c.execute("select * from cars")
        car = c.fetchone()
        c1 = db.cursor()
        c1.execute(f'select user_id, review from reviews where car_id = {car_id}')
        reviews = c1.fetchall()

        return car, reviews

    def get_car_details1(self, car_id):
        c = db.cursor()
        query = f'select c.*, r.user_id, r.review , u.user_name from cars c ' \
                f'left join reviews r on c.cars_id = r.car_id' \
                f' left JOIN users u on u.id = r.user_id where c.cars_id = {car_id} '
        c.execute(query)
        out = c.fetchall()
        first_row = out[0]
        car = Car(first_row[0], first_row[1], first_row[2], first_row[3], first_row[4])
        reviews = map(lambda row: Review(row[7], car_id, row[6]), out)
        return car, reviews

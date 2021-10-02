from models.Car import Car
from models.Review import Review
from servcies.ServiceBase import ServiceBase
from models.Cars_image_gallery import Gallery


class CarService(ServiceBase):

    def show_cars(self):
        c = self.db.cursor()
        all_cars = "select id, make, name, year, image, avg_review from cars"
        c.execute(all_cars)
        rows = c.fetchall()
        # imperative style
        # cars = []
        # for row in rows:
        #    cars.append(Car(_id=row[0], make=row[1], name=row[2], year=row[3], image=[4], avg_review=row[5]))
        # functional style
        return map(lambda row: Car(row[0], row[1], row[2], row[3], row[4], row[5]), rows)

    def get_car_details(self, car_id):
        self.connect()
        c_id = int(car_id)
        c = self.db.cursor()
        query = f"""select c.id, c.name, r.user_id, r.*, u.name from cars c
                left join reviews r on c.id = r.car_id
                left JOIN users u on u.id = r.user_id where c.id = {c_id} """
        c.execute(query)
        out = c.fetchall()
        first_row = out[0]
        car = Car(_id=first_row[0], name=first_row[1], make='', image='', avg_review=0.0, year=0000)
        reviews = list(map(lambda row: Review(user_id=row[2], car_id=row[0], all_review=row[3], engine_review=row[6],
                                              comfort_review=row[7], fuel_review=row[8], stability_review=row[9],
                                              safety_review=row[10], technology_review=row[11], user_comment=row[12],
                                              user_name=row[13]), out))
        c.close()
        return car, reviews

    def get_car_img(self, car_id):
        self.connect()
        car_id = int(car_id)
        c = self.db.cursor()
        query = f"select img FROM cars.images where car_id = {car_id}"
        c.execute(query)
        out = c.fetchall()
        c.close()
        car_image = []
        for image in out:
            car_image.append(Gallery(image=image))
        return car_image

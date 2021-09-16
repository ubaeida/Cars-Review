from models.Car import Car
from models.Review import Review
from servcies.ServiceBase import ServiceBase
from models.imge import imge

all_cars = "select id, make, name, year, image from cars"


class CarService(ServiceBase):

    def show_cars(self):
        c = self.db.cursor()
        c.execute(all_cars)
        rows = c.fetchall()
        # imperative style
        # cars = []
        # for row in rows:
        #    cars.append(Car(row[0], row[1], row[2], row[3], row[4]))

        # functional style
        return map(lambda row: Car(row[0], row[1], row[2], row[3], row[4]), rows)

    def get_car_details(self, car_id):
        self.connect()
        c_id = int(car_id)
        c = self.db.cursor()
        query = f"""select c.id, c.name, r.user_id, r.review, u.name from cars c
                left join reviews r on c.id = r.car_id
                left JOIN users u on u.id = r.user_id where c.id = {c_id} """
        c.execute(query)
        out = c.fetchall()
        first_row = out[0]
        car = Car(_id=first_row[0], name=first_row[1], make='', image='', year=0000)
        reviews = list(map(lambda row: Review(row[2], c_id, row[3], user_name=row[4]), out))
        c.close()
        return car, list(filter(None, reviews))

    def get_car_img(self, car_id):
        self.connect()
        car_id = int(car_id)
        c = self.db.cursor()
        query = f"select img FROM cars.images where car_id = {car_id}"
        c.execute(query)
        out = c.fetchall()
        images = []
        for row in out:
            print(row)
            images.append(imge(img=row))
        return images

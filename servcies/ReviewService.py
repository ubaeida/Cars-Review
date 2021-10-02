from models.Review import Review
from servcies.ServiceBase import ServiceBase
import numpy


class ReviewService(ServiceBase):

    def get_review(self, user_id, car_id):
        c = self.db.cursor()
        query = "select * from reviews where user_id= %s and car_id = %s"
        params = (user_id, int(car_id))
        c.execute(query, params)
        out = c.fetchall()
        c.close()
        for row in out:
            if row is not None:
                print('searched review')
                return Review(all_review=row[0], car_id=row[1], user_id=row[2], engine_review=row[3],
                              comfort_review=row[4], fuel_review=row[5], stability_review=row[6], safety_review=row[7],
                              technology_review=row[8], user_comment=row[9], user_name='')
        return None

    def get_review_avg(self, car_id):
        self.connect()
        c = self.db.cursor()
        avg_query = f'select all_review from reviews where car_id = {car_id};'
        c.execute(avg_query)
        out = c.fetchall()
        review_avg = numpy.mean(out)
        avg = format(review_avg, ".1f")
        c.close()
        return avg

    def add_review(self, user_id, car_id, all_review, engine_review, comfort_review,
                   fuel_review, stability_review, safety_review, technology_review, user_comment):
        self.connect()
        user_id = int(user_id)
        car_id = int(car_id)
        all_review = int(all_review)
        engine_review = int(engine_review)
        comfort_review = int(comfort_review)
        fuel_review = int(fuel_review)
        stability_review = int(stability_review)
        safety_review = int(safety_review)
        technology_review = int(technology_review)
        user_comment = str(user_comment)
        old_review = self.get_review(user_id, car_id)
        if old_review is None:
            query = "insert into reviews " \
                    "(user_id, car_id, all_review, engine_review, comfort_review," \
                    "fuel_review, stability_review, safety_review, technology_review, user_comment)" \
                    f" values ({user_id}, {car_id}, {all_review}, {engine_review}, {comfort_review},{fuel_review}, " \
                    f"{stability_review}, {safety_review}, {technology_review}, {user_comment})"
            avg = self.get_review_avg(car_id=car_id)
            insert_query = f'update cars set avg_review = {avg} where id={car_id}'
        else:
            query = f'update reviews set all_review = {all_review}, engine_review = {engine_review},' \
                    f' comfort_review = {comfort_review}, fuel_review = {fuel_review}, stability_review = {stability_review},' \
                    f' safety_review = {safety_review}, technology_review = {technology_review}, user_comment = {user_comment}' \
                    f' where user_id = {user_id} and car_id = {car_id}'
            avg = self.get_review_avg(car_id=car_id)
            insert_query = f'update cars.cars set avg_review = {avg} where id={car_id}'
        c = self.db.cursor()
        c.execute(query)
        c.execute(insert_query)
        c.close()
        self.db.commit()
        self.db.close()

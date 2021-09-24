from models.Review import Review
from models.user import User
from servcies.ServiceBase import ServiceBase


class UserService(ServiceBase):

    def register_user(self, username, password, name, email):
        self.connect()
        c = self.db.cursor()
        reg = f"insert into users  (username, password, name, email) values (%s, %s, %s, %s)"
        c.execute(reg, (username, password, name, email))
        self.db.commit()

    def user_log_in(self, username, password):
        self.connect()
        c = self.db.cursor()
        log = f"select id, username, password, name, email from users where username= '{username}' and password = '{password}' "
        c.execute(log)
        out = c.fetchall()
        for row in out:
            if row is not None:
                return User(row[0], row[1], row[2], row[3], row[4])
        return None

    def get_review(self, user_id, car_id):
        c = self.db.cursor()
        query = "select * from reviews where user_id= %s and car_id = %s"
        params = (user_id, int(car_id))
        c.execute(query, params)
        out = c.fetchall()
        print(out)
        c.close()
        for row in out:
            if row is not None:
                print('searched review')
                return Review(all_review=row[0], car_id=row[1], user_id=row[2], engine_review=row[3],
                              comfort_review=row[4], fuel_review=row[5],
                              stability_review=row[6], safety_review=row[7], technology_review=row[8], user_name='')
        return None

    def add_review(self, user_id, car_id, all_review, engine_review, comfort_review,
                   fuel_review, stability_review, safety_review, technology_review):
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
        old_review = self.get_review(user_id, car_id)
        if old_review is None:
            query = "insert into reviews " \
                    "(user_id, car_id, all_review, engine_review, comfort_review," \
                    "fuel_review, stability_review, safety_review, technology_review )" \
                    f" values ({user_id}, {car_id}, {all_review}, {engine_review}, {comfort_review},{fuel_review}, " \
                    f"{stability_review}, {safety_review}, {technology_review})"
        else:
            query = f'update reviews set all_review = {all_review}, engine_review = {engine_review},' \
                    f' comfort_review = {comfort_review},fuel_review = {fuel_review}, stability_review = {stability_review},' \
                    f' safety_review = {safety_review}, technology_review = {technology_review}' \
                    f' where user_id = {user_id} and car_id = {car_id}'
        c = self.db.cursor()
        c.execute(query)
        c.close()
        self.db.commit()
        self.db.close()

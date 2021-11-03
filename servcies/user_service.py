from models.user import User
from servcies.ServiceBase import ServiceBase
from models.User_activity import UserActivity
from models.Review import Review


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
        old_review = self.get_review(user_id, car_id)
        if old_review is None:
            query = "insert into reviews " \
                    "(user_id, car_id, all_review, engine_review, comfort_review," \
                    "fuel_review, stability_review, safety_review, technology_review )" \
                    " values (%s , %s , %s , %s , %s , %s , %s , %s , %s)"
            params = (user_id, car_id, all_review, engine_review, comfort_review,
                      fuel_review, stability_review, safety_review, technology_review)
        else:
            params = (user_id, car_id, all_review, engine_review, comfort_review,
                      fuel_review, stability_review, safety_review, technology_review)
            query = 'update reviews set all_review = %s, engine_review = %s, comfort_review = %s, ' \
                    'fuel_review = %s, stability_review = %s, safety_review = %s, technology_review = %s' \
                    ' where user_id = %s and car_id = %s'
        c = self.db.cursor()
        c.execute(query, params)
        c.close()
        self.db.commit()
        self.db.close()

    def user_profile(self, user_id):
        self.connect()
        query = f'SELECT * FROM cars.users where id = {user_id}'
        c = self.db.cursor()
        c.execute(query)
        out = c.fetchall()
        c.close()
        for row in out:
            if row is not None:
                return User(_id=row[0], username=row[1], password='****', name=row[3], email=row[4])
        return None

    def user_activity(self, user_id):
        def review_from_row(row):
            return Review(all_review=row[1], engine_review=row[4], comfort_review=row[5],
                          fuel_review=row[6], stability_review=row[7], safety_review=row[8],
                          technology_review=row[9], car_id=row[2], user_id=row[3],
                          user_comment=row[10], user_name='')

        self.connect()
        query = f"""select u.id , r.* , c.name from users u left join
                reviews r on u.id = r.user_id left join cars c on r.car_id = c.id  where user_id = {user_id} """
        c = self.db.cursor()
        c.execute(query)
        out = c.fetchall()
        c.close()
        activities = map(lambda row: UserActivity(user_id, row[11], review_from_row(row)), out)
        return activities

    def update_profile(self, username, name, email, old_password, new_password, user_id):
        self.connect()
        query = f""" SELECT username, password, name, email FROM users where id = {user_id} """
        c = self.db.cursor()
        c.execute(query)
        out = c.fetchall()
        if out[0][1] == old_password and out is not None:
            query1 = f""" update users set username= '{username}', name= '{name}', 
            email= '{email}', password= '{new_password}' where id= {user_id} """
            c.execute(query1)
        self.db.commit()

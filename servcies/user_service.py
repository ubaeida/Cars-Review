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
        c.close()
        for row in out:
            if row is not None:
                print('searched review')
                return Review(row[0], row[1], row[2], user_name='')
        return None

    def add_review(self, user_id, car_id, review):
        self.connect()
        user_id = int(user_id)
        car_id = int(car_id)
        review = int(review)
        old_review = self.get_review(user_id, car_id)
        if old_review is None:
            query = "insert into reviews ( user_id, car_id, review) values (%s , %s , %s)"
            params = (user_id, car_id, review)
            print(query % params)
        else:
            params = (review, user_id, car_id)
            query = 'update reviews set review = %s where user_id = %s and car_id = %s'
            print(query % params)

        c = self.db.cursor()
        c.execute(query, params)
        c.close()
        self.db.commit()
        self.db.close()

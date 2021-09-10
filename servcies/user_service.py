from mysql.connector import (connection)
from models.Review import Review
from models.user import User

db = connection.MySQLConnection(user='root', password='newpass',
                              host='127.0.0.1',
                              database='cars')

class UserService:

    def register_user(self, username, password):

        c = db.cursor()
        reg = f"insert into users  (user_name, password) values ('{username}', '{password}')"
        c.execute(reg)
        db.commit()

    def user_log_in(self, username, password):

        c = db.cursor()
        log = f"select * from users where user_name= '{username}' and password = '{password}' "
        c.execute(log)
        out = c.fetchall()
        for row in out:
            if row is not None:
                return User(row[0], row[1], row[2])
        return None

    def get_review(self, user_id, car_id):
        c = db.cursor()
        query = "select * from reviews where user_id= ? and car_id = ? "
        params = (user_id, car_id)
        out = c.execute(query, params)
        for row in out:
            if row is not None:
                return Review(row[0], row[1], row[2])
        return None

    def add_review(self, user_id, car_id, review):
        old_review = self.get_review(user_id, car_id)
        c = db.cursor()
        if old_review is None:
            query = "insert into reviews (review, car_id, user_id) values (%s , %s , %s)"
            params = (user_id, car_id, review)
        else:
            params = (review, user_id, car_id)
            query = 'update reviews set review = %s where user_id = %s and car_id = %s'

        c.execute(query, params)
        db.commit()
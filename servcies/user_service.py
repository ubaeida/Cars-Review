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

import mysql.connector


class ServiceBase:
    def __init__(self):
        self.db = mysql.connector.connect(user='root', password='123456',
                                          host='127.0.0.1',
                                          database='cars', auth_plugin='mysql_native_password')

    def connect(self):
        self.db = mysql.connector.connect(user='root', password='123456',
                                          host='127.0.0.1',
                                          database='cars', auth_plugin='mysql_native_password')

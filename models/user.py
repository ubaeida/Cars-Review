class User:
    def __init__(self, _id, username, password, name, email):
        self.myid = _id
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __str__(self):
        return f'_id: {self.myid}, username: {self.username}, password: {self.password}, name: {self.name},' \
               f' email: {self.email}'

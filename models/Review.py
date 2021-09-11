class Review:
    def __init__(self, user_id, car_id, review, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.car_id = car_id
        self.review = review


    def __str__(self):
        return f'car: {self.car_id}, review: {self.review}'

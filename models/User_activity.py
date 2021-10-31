from models.Review import Review


class UserActivity:
    def __init__(self, user_id, car_name, review: Review):
        self.user_id = user_id
        self.car_name = car_name
        self.review = review

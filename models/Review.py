class Review:
    def __init__(self, user_id, car_id, all_review, user_name, engine_review, comfort_review, fuel_review,
                 stability_review, safety_review, technology_review):
        self.user_id = user_id
        self.user_name = user_name
        self.car_id = car_id
        self.all_review = all_review
        self.engine_review = engine_review
        self.comfort_review = comfort_review
        self.fuel_review = fuel_review
        self.stability_review = stability_review
        self.safety_review = safety_review
        self.technology_review = technology_review

    def __str__(self):
        return f'car: {self.car_id}, all_review: {self.all_review}, engine_review: {self.engine_review},' \
               f' comfort_review: {self.comfort_review}, fuel_review: {self.fuel_review}, ' \
               f'stability_review: {self.stability_review}, safety_review{self.safety_review}, ' \
               f'technology_review: {self.technology_review}'

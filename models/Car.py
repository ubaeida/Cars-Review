class Car:
    def __init__(self, _id, make, name, year, image, avg_review):
        self.id = _id
        self.make = make
        self.name = name
        self.year = year
        self.image = image
        self.avg_review = avg_review

    def __str__(self):
        return f'{self.name}'

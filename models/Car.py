class Car:
    def __init__(self, _id, make, name, year, image):
        self.id = _id
        self.make = make
        self.name = name
        self.year = year
        self.image = image

    def __str__(self):
        return f'{self.name}'

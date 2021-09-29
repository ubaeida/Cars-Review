class CarAttribute:

    def __init__(self, car_id, attribute_id, attribute_name, value_id, value):
        self.car_id = car_id
        self.attribute_id = attribute_id
        self.attribute_name = attribute_name
        self.value_id = value_id
        self.value = value

    def __str__(self):
        return f'attribute_name: {self.attribute_name}, Value: {self.value}, attribute_id: {self.attribute_id},' \
               f' value_id: {self.value_id}, car_id: {self.car_id}'

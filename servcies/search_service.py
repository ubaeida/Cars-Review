from models.Search import Search
from servcies.ServiceBase import ServiceBase


class SearchService(ServiceBase):

    def searching(self, car_make, car_model, year):

        print(car_make, car_model, year)

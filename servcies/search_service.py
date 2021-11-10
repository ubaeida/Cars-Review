from models.Search import Search
from servcies.ServiceBase import ServiceBase
from models.Car import Car


class SearchService(ServiceBase):

    def searching(self, car_name, car_model, year):
        self.connect()
        c = self.db.cursor()

        query = f"""
                select * from cars where name like '%{car_name}%' and make like '%{car_model}%' and year like '%{year}%'
                """
        c.execute(query)
        out = c.fetchall()
        c.close()
        print(out)
        results = map(lambda row: Car(_id=row[0], make=row[1], year=row[2], image=row[3], name=row[4],
                                      avg_review=row[5]), out)
        return results

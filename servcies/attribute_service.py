from models.Car_attribute import CarAttribute
from servcies.ServiceBase import ServiceBase


class AttributeService(ServiceBase):

    def get_attributes(self, car_id):
        c = self.db.cursor()
        query = "select a.id,a.name,a.data_type,a.allowed_values, ca.value from car_attributes ca left join attributes a " \
                f"on a.id = ca.attribute_id where car_id= {car_id}"
        print(f"-------\n{query}\n-------\n")
        c.execute(query)
        out = c.fetchall()
        c.close()
        attribute_list = []
        for row in out:
            attribute_list.append(CarAttribute(car_id=car_id, attribute_id=row[0], attribute_name=row[1], data_type=row[2],
                                               allowed_values=row[3].split(','), value=row[4]))
        return attribute_list

from models.Car_attribute import CarAttribute
from servcies.ServiceBase import ServiceBase


class AttributeService(ServiceBase):

    def show_attribute(self, car_id):
        c = self.db.cursor()
        query = "select v.*, a.attribute_name from attribute_value v left join car_attribute a " \
                f"on a.id = v.attribute_id where car_id= {car_id}"
        print(f"-------\n{query}\n-------\n")
        c.execute(query)
        out = c.fetchall()
        c.close()
        attribute_list = []
        for row in out:
            attribute_list.append(CarAttribute(value_id=row[0], car_id=row[1], attribute_id=row[2], value=row[3],
                                               attribute_name=row[4]))
        return attribute_list

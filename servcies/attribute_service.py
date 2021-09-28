from models.Car_attribute import CarAttribute
from servcies.ServiceBase import ServiceBase


class AttributeService(ServiceBase):

    def show_attribute(self, car_id):
        c = self.db.cursor()
        query = "select v.*, a.attribute_name from attribute_value v left join car_attribute a " \
                f"on a.id = v.attribute_id where car_id= {car_id}"
        params = (int(car_id))
        c.execute(query)
        out = c.fetchall()
        print(out)
        for row in out:
            if row is not None:
                print('searched attribute')
                return CarAttribute(value_id=row[0], attribute_id=row[2], value=row[3], attribute_name=row[4])
        return None

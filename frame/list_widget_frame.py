from frame.CSS_template import BaseClassWidget
from dbase.dbapi import APIAxiomDB
from log_setting import logger


class ListWOrder(BaseClassWidget):
    text = 'Заказ-Наряд'
    size = 250
    template = {
        'pattern': '  {} - {}    : {}'
    }
    query = APIAxiomDB()
    temp_list = [str(idnum.id) for idnum in query.get_list_order()]

    def __int__(self, size=200):
        super(ListWOrder, self).__int__()

    @logger.catch
    def get_item_text_from_list(self, item):
        temp = item.text().split('-')
        temp_list = self.query.get_order_from_id(temp[0])
        return temp_list

    @logger.catch
    def print(self):
        self.clear_items()
        order_item_list = [ListWOrder.template['pattern'].format(elem.id, elem.prefix, elem.data)
                for elem in self.query.get_list_order()]
        self.set_items(order_item_list)

    def print_one(self):
        pass

    @logger.catch
    def print_widget(self, name, foo='clt'):
        self.clear_items()
        order_item_list = []
        if foo == 'clt':
            order_item_list = [ListWOrder.template['pattern'].format(elem.id, elem.prefix, elem.data)
                    for elem in self.query.get_client_list_order(name)]
        elif foo == 'car':
            order_item_list = [ListWOrder.template['pattern'].format(elem.id, elem.prefix, elem.data)
                    for elem in self.query.get_car_list_order(name)]
        self.set_items(order_item_list)


class ListWClient(BaseClassWidget):
    text = 'Клиент'
    size = 250
    query = APIAxiomDB()
    temp_list = [name.lower() for name in query.get_list_company()]

    def __int__(self, size=200):
        super(ListWClient, self).__int__()

    @logger.catch
    def print(self):
        self.clear_items()
        client_item_list = self.query.get_list_company()
        self.set_items(client_item_list)

    @logger.catch
    def print_one(self, id_num: int):
        self.clear_items()
        client_item = self.query.get_client_from_order(id_num)
        self.set_item(client_item.name)

    @logger.catch
    def print_widget(self, client_item):
        self.clear_items()
        self.set_item(client_item.name)

    @logger.catch
    def get_item_text_from_list(self, item):
        client_item_list = self.query.get_client_from_name(item.text())
        return client_item_list


class ListWCar(BaseClassWidget):
    text = 'Car'
    size = 330
    template = {
        'pattern': '{}  | {} | {}-{}'
    }
    query = APIAxiomDB()
    temp_list = [car.number for car in query.get_list_car()]

    # def __int__(self, size=350):
    #     super(ListWCar, self).__int__()

    @logger.catch
    def print(self):
        self.clear_items()

        car_item_list = [ListWCar.template['pattern'].format(elem.id, elem.number, elem.name, elem.model)
                for elem in self.query.get_list_car()
                         if elem.name != 'Запчасти']
        self.set_items(car_item_list)

    @logger.catch
    def print_one(self, id_num: int):
        self.clear_items()
        car_item = self.query.get_car_from_order(id_num)
        self.set_item(ListWCar.template['pattern'].format(car_item.id, car_item.number, car_item.name, car_item.model))

    @logger.catch
    def print_widget(self, name):
        self.clear_items()
        car_item_list = [ListWCar.template['pattern'].format(elem.id, elem.number, elem.name, elem.model)
                for elem in self.query.get_client_list_car(name)
                         if elem.name != 'Запчасти']
        self.set_items(car_item_list)

    @logger.catch
    def get_item_text_from_list(self, item: str):
        elem = item.split()
        car_item = self.query.get_car_from_id(int(elem[0]))
        return car_item


if __name__ == "__main__":
    pass

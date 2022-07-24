from CSS_template import BaseClassWidget
from dbapi import APIAxiomDB


class ListWOrder(BaseClassWidget):
    text = 'Заказ-Наряд'
    size = 200
    spis = []

    def __int__(self):
        super(ListWOrder, self).__int__()

    def get_item_text_from_list(self, item):
        new = APIAxiomDB()
        temp = item.text().split('-')
        temp_list = new.get_order_from_id(temp[0])
        return temp_list

    def print(self):
        self.clear_items()
        new = APIAxiomDB()
        temp = ['  {} - {}    : {}'.format(elem.id, elem.prefix, elem.data) for elem in new.get_list_order()]
        self.set_items(temp)

    def print_widget(self, name, foo='clt'):
        self.clear_items()
        new = APIAxiomDB()
        temp = None
        if foo == 'clt':
            temp = ['  {} - {}    : {}'.format(elem.id, elem.prefix, elem.data) for elem in new.get_client_list_order(name)]
        elif foo == 'car':
            temp = ['  {} - {}    : {}'.format(elem.id, elem.prefix, elem.data) for elem in new.get_car_list_order(name)]
        self.set_items(temp)


class ListWClient(BaseClassWidget):
    text = 'Клиент'
    size = 220
    spis = []

    def __int__(self):
        super(ListWClient, self).__int__()

    def print(self):
        self.clear_items()
        new = APIAxiomDB()
        temp = new.get_list_company()
        self.set_items(temp)

    def print_one(self, id_num: int):
        self.clear_items()
        new = APIAxiomDB()
        temp = new.get_client_from_order(id_num)
        self.set_item(temp.name)

    def get_item_text_from_list(self, item):
        new = APIAxiomDB()
        temp_list = new.get_client_from_name(item.text())
        return temp_list

    # def print_widget(self, name):
    #     self.clear_items()
    #     new = APIAxiomDB()
    #     temp = ['{} | {}-{}'.format(elem[2],elem[0],elem[1]) for elem in new.get_client_list_car(name)]
    #     self.set_items(temp)


class ListWCar(BaseClassWidget):
    text = 'Car'
    size = 420
    spis = ['maz', 'zil', 'volga', 'mazda', 'leksus']

    def __int__(self):
        super(ListWCar, self).__int__()

    def print(self):
        self.clear_items()
        new = APIAxiomDB()
        temp = ['{}  |  №- {} | {}-{}'.format(elem.id, elem.number, elem.name, elem.model)
                for elem in new.get_list_car()]
        self.set_items(temp)

    def print_widget(self, name):
        self.clear_items()
        new = APIAxiomDB()
        temp = ['{}  |  №- {} | {}-{}'.format(elem.id, elem.number, elem.name, elem.model)
                for elem in new.get_client_list_car(name)]
        self.set_items(temp)

    def print_one(self, id_num: int):
        self.clear_items()
        new = APIAxiomDB()
        temp = new.get_car_from_order(id_num)
        self.set_item('{}  |  №- {} | {}-{}'.format(temp.id, temp.number, temp.name, temp.model))

    def get_item_text_from_list(self, item: str):
        new = APIAxiomDB()
        elem = item.split()
        temp_list = new.get_car_from_id(int(elem[0]))
        return temp_list


if __name__ == "__main__":
    pass

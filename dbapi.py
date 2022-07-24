from typing import Any

from dbbaseinit import CompanyDB
from dbbaseinit import CarDB
from dbbaseinit import OrderDB
from dbbaseinit import db
from databasecreate import CreateDB


class APIAxiomDB:
    """Предоставляет механизм получения запросов из базы данных."""

    @classmethod
    def get_client_from_name(cls, name: (str, int)) -> Any:
        """Получение списка полей клиента по его короткому наименованию или по его идентификационному номеру."""

        with db:
            if isinstance(name, int):
                temp = CompanyDB.get(CompanyDB.id == name)
            else:
                temp = CompanyDB.get(CompanyDB.name == name)
            temp_list = [
                        temp.id,
                        temp.name,
                        temp.full_name,
                        temp.address,
                        temp.pan_code,
                        temp.telefone,
                        temp.mobile,
                        temp.driver_name,
                        temp.driver_job
            ]
            return temp

    @classmethod
    def get_client_from_unp(cls, unp: int) -> Any:
        """Получение списка полей клиента по его УНП."""

        with db:
            temp = CompanyDB.get(CompanyDB.pan_code == unp)
            temp_list = [
                temp.id,
                temp.name,
                temp.full_name,
                temp.address,
                temp.pan_code,
                temp.telefone,
                temp.mobile,
                temp.driver_name,
                temp.driver_job
            ]
            return temp

    @classmethod
    def get_order_from_id(cls, name: int) -> Any:
        """Получение списка полей Акта по его идентификационному номеру из базы данных ."""

        with db:
            temp = OrderDB.get(OrderDB.id == name)
            temp_list = [
                        temp.id,
                        temp.car_id,
                        temp.company_id,
                        temp.prefix,
                        temp.data,
                        temp.closing_mark,
                        temp.first_open,
                        temp.data_close,
                        temp.path_file
            ]
            return temp

    @classmethod
    def get_car_from_id(cls, name: (str, int)) -> Any:
        """Получение списка полей машины клиента по его номеру или идентификационному номеру из базы данных ."""

        with db:
            if isinstance(name, int):
                temp = CarDB.get(CarDB.id == name)
            else:
                temp = CarDB.get(CarDB.number == name)
            temp_list = [
                        temp.id,
                        temp.name,
                        temp.model,
                        temp.number,
                        temp.vin_code,
                        temp.company_id
            ]
            return temp

    @classmethod
    def get_list_company(cls) -> list:
        """Получение полного списка клиентов из базы данных."""
        temp_list = []
        with db:
            for elem in CompanyDB.select():
                temp_list.append(elem.name)
        return temp_list

    @classmethod
    def get_list_car(cls) -> list:
        """Получение полного списка машин из базы данных."""
        temp_list = []
        with db:
            for elem in CarDB.select():
                temp_list.append(elem)
        return temp_list

    @classmethod
    def get_list_order(cls) -> list:
        """Получение полного списка текущих (открытых) актов из базы данных."""

        temp_list = []
        with db:
            for elem in OrderDB.select().where(OrderDB.closing_mark == False):
                temp_list.append(elem)
        return temp_list

    @classmethod
    def get_list_old_order(cls) -> list:
        """Получение полного списка закрытых актов из базы данных."""

        temp_list = []
        with db:
            for elem in OrderDB.select().where(OrderDB.closing_mark == True):
                temp_list.append((elem.id, elem.prefix, elem.data))
        return temp_list

    @classmethod
    def get_client_list_car(cls, name: (str, int)) -> list:
        """Получение полного списка машин клиента, заданного по короткому имени или идентификационному номеру, 
        из базы данных.
        """

        temp_list = []
        with db:
            if isinstance(name, int):
                temp = CarDB.select().where(CarDB.company_id == CompanyDB.select().where(CompanyDB.id == name))
            else:
                temp = CarDB.select().where(CarDB.company_id == CompanyDB.select().where(CompanyDB.name == name))
            for elem in temp:
                temp_list.append(elem)
        return temp_list

    @classmethod
    def get_car_list_order(cls, name: (str, int)) -> Any:
        """Получение полного списка открытых актов на машину, заданной по номеру или идентификационному номеру,
        из базы данных.
        """

        temp_list = []
        with db:
            if isinstance(name, int):
                temp = OrderDB.select().where(OrderDB.car_id == CarDB.select()
                                              .where(CarDB.id == name))
            else:
                temp = OrderDB.select().where(OrderDB.car_id == CarDB.select()
                                              .where(CarDB.number == name))
            for elem in temp:
                if not elem.closing_mark:
                    temp_list.append(elem)
        return temp_list

    @classmethod
    def get_client_list_order(cls, name: (str, int)) -> Any:
        """Получение полного списка актов клиента, заданного по короткому имени или идентификационному номеру, 
        из базы данных.
        """

        temp_list = []
        with db:
            if isinstance(name, int):
                temp = OrderDB.select().where(OrderDB.company_id == CompanyDB.select()
                                              .where(CompanyDB.id == name))
            else:
                temp = OrderDB.select().where(OrderDB.company_id == CompanyDB.select()
                                              .where(CompanyDB.name == name))
            for elem in temp:
                if not elem.closing_mark:
                    temp_list.append(elem)
        return temp_list

    @classmethod
    def get_client_list_order_from_name(cls, name: (str, int)) -> list:
        """Получение полного списка актов клиента с указанием машин в этих актах,
         заданного по короткому имени или идентификационному номеру, из базы данных.
         """

        temp_list = []
        with db:
            if isinstance(name, int):
                temp = OrderDB.select().where(OrderDB.company_id == CompanyDB.select().where(CompanyDB.id == name))
            else:
                temp = OrderDB.select().where(OrderDB.company_id == CompanyDB.select().where(CompanyDB.name == name))
            for elem in temp:
                car = CarDB.get(CarDB.id == elem.car_id)
                temp_list.append(
                    (elem.id, elem.prefix, elem.data, car.name, car.model, car.number))
        return temp_list

    @classmethod
    def get_client_from_order(cls, id_num):
        with db:
            temp = CompanyDB.get(CompanyDB.id == OrderDB.get(OrderDB.id == id_num).company_id)
        return temp

    @classmethod
    def get_car_from_order(cls, id_num):
        with db:
            temp = CarDB.get(CarDB.id == OrderDB.get(OrderDB.id == id_num).car_id)
        return temp

    @classmethod
    def count_act(cls):
        with db:
            temp = OrderDB.select().count()
        return temp


if __name__ == '__main__':
    NEW = CreateDB()
    # NEW.update_prefix(5)
    # NEW.change_car(4, brand='МАЗ', model='4431', number='32-15')

    # NEW.car_create(
    #     name='MAZ',
    #     model='6422',
    #     number='34-15',
    #     company_id=2
    # )

    new_act = APIAxiomDB()
    # print(new_act.count_act())

    a = new_act.get_client_from_order(1)
    print(a)
    b = new_act.get_car_from_order(1)[1]
    print(b)
    c = new_act.get_client_list_car('SGP')
    print(c)
    d = new_act.get_client_list_order_from_name('SGP')
    for elem in d:
        print(elem)

from peewee import IntegrityError

from dbbaseinit import CompanyDB
from dbbaseinit import CarDB
from dbbaseinit import OrderDB
from dbbaseinit import Driver
from dbbaseinit import db
from datetime import datetime
from datetime import date


class CreateDB:
    """Создание базы данных.

    Внесение новых записей: клиент, машина клиента, акты.
    Работа с базой данных по изменениям записей:
    изменение префикса номера акта,
    изменение отметки о первом открытии акта,
    изменение отметки о закрытии акта и установка даты закрытия,
    внесение изменений о данных машины клиента,
    внесение изменений о данных клиента.

    """

    def __int__(self):
        pass

    @classmethod
    def create_db(cls) -> None:
        """Создание новой базы данных."""
        with db:
            db.create_tables(
                [CompanyDB, CarDB, OrderDB, Driver], safe=True
            )

    @classmethod
    def driver_create(
            cls,
            name: str = '',
            job: str = '',
            company_id: int = None
    ) -> None:
        try:
            with db:
                new = CompanyDB(
                    name=name,
                    job=job,
                    company_id=company_id
                )
                new.save()
        except IntegrityError as err:
            print('запись водителя с таким именем уже есть. ', err)

    @classmethod
    def company_create(
            cls,
            name: str = '',
            full_name: str = '',
            address: str = '',
            pan_code: int = None,
            telefone: str = '',
            mobile: str = '',
            driver_name: str = '',
            driver_job: str = ''
    ) -> None:
        """Добавление нового клиента в базу данных."""

        try:
            with db:
                new = CompanyDB(
                    name=name,
                    full_name=full_name,
                    address=address,
                    pan_code=pan_code,
                    telefone=telefone,
                    mobile=mobile,
                    driver_name=driver_name,
                    driver_job=driver_job
                )
                new.save()
        except IntegrityError as err:
            print('запись клиента с таким УНП уже есть. ', err)

    @classmethod
    def car_create(
            cls,
            name: str = '',
            model: str = '',
            number: str = '',
            vin_code: str = '',
            company_id: int = None
    ) -> None:
        """Устанавливает новую запись о машине клиента в базу данных."""

        try:
            with db:
                new = CarDB(
                    name=name,
                    model=model,
                    number=number,
                    vin_code=vin_code,
                    company_id=company_id
                )
                new.save()
        except IntegrityError as err:
            print('запись машины с таким номером уже есть. ', err)
        except ValueError as err:
            print('Ошибка. ', err)

    @classmethod
    def order_create(
            cls,
            car_id: int = None,
            company_id: int = None,
            prefix: str = '',
            data: date = datetime.now(),
            closing_mark: bool = False,
            first_open: bool = False,
            data_close: date = None,
            path_file: str = ''
    ) -> None:
        """Устанавливает новую запись об открытии нового акта в базу данных."""

        try:
            with db:
                new = OrderDB(
                    car_id=car_id,
                    company_id=company_id,
                    prefix=prefix,
                    data=data,
                    closing_mark=closing_mark,
                    first_open=first_open,
                    data_close=data_close,
                    path_file=path_file
                )
                new.save()
        except IntegrityError as err:
            print('запись акта с таким номером уже есть. ', err)

    @classmethod
    def update_prefix(cls, id: int):
        """Увеличивает значение префикса номера акта на единицу"""

        with db:
            upd = OrderDB.get(OrderDB.id == id)
            upd.prefix = chr(ord(upd.prefix) + 1)
            upd.save()

    @classmethod
    def close_order(cls, id: int, foo: bool):
        """
        Изменяет метку о закрытии акта на True.
        Нужно, чтобы убрать акт из списка текущих актов.
        По метке будет выводиться мписок сохраненных и закрытых актов.
        """

        with db:
            upd = OrderDB.update(closing_mark=foo, data_close=datetime.now().date()).where(OrderDB.id == id)
            upd.execute()

    @classmethod
    def first_open_close(cls, id: int):
        """Изменяет метку о первом открытии акта на False.
        Нужно, чтобы изменить условие печати документов.
        """

        with db:
            upd = OrderDB.update(first_open=False).where(OrderDB.id == id)
            upd.execute()

    @classmethod
    def isClose(cls, id: int):
        """Вщзвращает состояние акта
        """

        with db:
            upd = OrderDB.get(OrderDB.id == id)
            return upd.closing_mark

    @classmethod
    def update_car(cls, id: int, name: str, model: str, number: str, vin_code: str):
        """Изменяет данные о машине"""

        try:
            with db:
                upd = CarDB.update(name=name, model=model, number=number, vin_code=vin_code).where(CarDB.id == id)
                upd.execute()
        except IntegrityError as err:
            print('машина с таким номером уже есть. ', err)

    @classmethod
    def update_client(
            cls,
            id: int,
            name: str,
            full_name: str,
            address: str = '',
            telefone: str = '',
            mobile: str = ''
    ) -> None:
        """Изменяет данные о клиенте"""
        with db:
            upd = CompanyDB.update(
                name=name,
                full_name=full_name,
                address=address,
                telefone=telefone,
                mobile=mobile
            ).where(CompanyDB.id == id)
            upd.execute()

    @classmethod
    def update_client_driver(
            cls,
            id: int,
            driver_name: str = '',
            driver_job: str = ''
    ):
        with db:
            upd = CompanyDB.update(
                driver_name=driver_name,
                driver_job=driver_job
            ).where(CompanyDB.id == id)
            upd.execute()



if __name__ == "__main__":
    NEW = CreateDB()
    NEW.create_db()

    NEW.company_create(
        name='BAMS',
        full_name='BelAvtoMazServis',
        address='Minsk',
        pan_code=100100100,
        mobile='',
        driver_name='',
        driver_job=''

    )
    NEW.company_create(
        name='SGP',
        full_name='ServisGarantPlus',
        address='Minsk',
        pan_code=230400400,
        telefone='12-22-22',
        driver_name='',
        driver_job=''
    )
    NEW.company_create(
        name='Gramd',
        full_name='Grandmotors',
        address='Mogilev',
        pan_code=899411333,
        telefone='12-22-22',
        mobile='8029444-44-44'
    )





    NEW.car_create(
        name='Volosiped',
        model='Sprinter',
        number='12-21',
        vin_code='UZM123123',
        company_id=1
    )
    NEW.car_create(
        name='MAZ',
        model='4371',
        number='56-18',
        vin_code='UZM437112',
        company_id=1
    )
    NEW.car_create(
        name='MAZ',
        model='5336',
        number='33-11',
        vin_code='UZM5336004',
        company_id=2
    )
    NEW.car_create(
        name='MAZ',
        model='6303',
        number='32-16',
        vin_code='UZM6303332',
        company_id=3
    )
    NEW.car_create(
        name='MAZ',
        model='6422',
        number='32-15',
        vin_code='UZM6422A5',
        company_id=2
    )
    NEW.car_create(
        name='MAZ',
        model='4371',
        number='44-44',
        vin_code='UZM4371005',
        company_id=3
    )




    NEW.order_create(
        car_id=5,
        company_id=2,
        prefix='A',
        closing_mark=False,
        first_open=False
    )
    NEW.order_create(
        car_id=6,
        company_id=3,
        prefix='A',
        data=datetime.now().date(),
        closing_mark=False,
        first_open=False,
        data_close=None,
        path_file='None'
    )


    NEW.order_create(
        car_id=1,
        company_id=1,
        prefix='A',
        data=datetime.now().date(),
        closing_mark=False,
        first_open=False,
        data_close=None,
        path_file='None'
    )

    NEW.order_create(
        car_id=4,
        company_id=3,
        prefix='A',
        data=datetime.now().date(),
        closing_mark=False,
        first_open=False,
        data_close=None,
        path_file='None'
    )

    NEW.order_create(
        car_id=3,
        company_id=2,
        prefix='A',
        data=datetime.now().date(),
        closing_mark=False,
        first_open=False,
        data_close=None,
        path_file='None'
    )

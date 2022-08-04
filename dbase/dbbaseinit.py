import os.path

from peewee import *
from datetime import datetime
from log_setting import config
from log_setting import logger

if os.path.exists(config['BASE']['specified_db']):
    db = SqliteDatabase(config['BASE']['db'])
else:
    db = SqliteDatabase(config['BASE']['db'])


class BaseModel(Model):
    id = AutoField()

    class Meta:
        database = db
        order_by = 'name'


class CompanyDB(BaseModel):
    name = TextField(null=False)
    full_name = TextField(null=False)
    pan_code = IntegerField(unique=True, null=False)
    address = TextField(null=True, default=None)
    telefone = TextField(null=True, default=None)
    mobile = TextField(null=True, default=None)

    class Meta:
        table_name = 'company_tbl'


class Driver(BaseModel):
    name = TextField(null=True, default=None)
    job = TextField(null=True, default=None)
    company_id = ForeignKeyField(CompanyDB)

    class Meta:
        table_name = 'driver_tbl'


class CarDB(BaseModel):
    name = TextField(null=False)
    model = TextField(null=False)
    number = TextField(unique=True, null=False)
    vin_code = TextField(null=False)
    company_id = ForeignKeyField(CompanyDB)

    class Meta:
        table_name = 'car_tbl'


class OrderDB(BaseModel):
    car_id = ForeignKeyField(CarDB)
    company_id = ForeignKeyField(CompanyDB)
    # number = IntegerField()
    prefix = CharField(default=chr(65))  # A
    data = DateField(null=True, default=datetime.now().date())
    closing_mark = BooleanField(default=False)
    first_open = BooleanField(default=True)
    data_close = DateField(null=True, default=None)
    path_file = TextField(null=True, default=None)
    driver_id = ForeignKeyField(Driver, null=True, default=None)

    class Meta:
        table_name = 'order_tbl'
        order_by = 'order_number'


if __name__ == '__main__':
    print(config['BASE']["db"])
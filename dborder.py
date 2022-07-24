from peewee import TextField, ForeignKeyField, IntegerField, DateField, BooleanField, CharField

from dbbaseinit import BaseModel
from datetime import datetime


class OrderDB(BaseModel):
    car_id = ForeignKeyField(BaseModel.CarDB)
    company_id = ForeignKeyField(BaseModel.CompanyDB)
    order_number = IntegerField(default=BaseModel.id)
    order_number_prefix = CharField(default='A')
    order_data = DateField(default=datetime.now())

    order_closing_mark = BooleanField(default=False)
    order_first_open = BooleanField(default=False)
    # order_count_act = IntegerField()
    # order_count_act_data = DateField()
    order_data_close = DateField(default=None)

    order_save_path_file = TextField(null=True, default=None)

    class Meta:
        table_name = 'order_tbl'
        order_by = 'order_number'

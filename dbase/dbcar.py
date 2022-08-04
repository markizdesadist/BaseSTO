from peewee import TextField, ForeignKeyField

from dbbaseinit import BaseModel


class CarDB(BaseModel):
    name = TextField(null=False)
    car_model = TextField(null=False)
    car_number = TextField(unique=True, null=False)
    company_id = ForeignKeyField(BaseModel.CompanyDB)

    class Meta:
        table_name = 'car_tbl'
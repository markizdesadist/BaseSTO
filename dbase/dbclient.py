from peewee import TextField, IntegerField

from dbbaseinit import BaseModel


class CompanyDB(BaseModel):
    name = TextField(null=False)
    company_full_name = TextField(null=False)
    company_pan_code = IntegerField(unique=True)
    company_address = TextField(null=True)
    company_telefone = TextField(null=True, default=None)
    company_mobile_phone = TextField(null=True, default=None)
    company_driver_name = TextField(null=True, default=None)
    company_driver_job = TextField(null=True, default=None)

    class Meta:
        table_name = 'company_tbl'
        order_by = 'name'
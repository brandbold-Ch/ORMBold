from models.model import Model
from utilities.sql_types import Functions


DATABASE_CONFIG = {
    "engine": "postgres",
    "user": "postgres",
    "dbname": "postgres",
    "host": "127.0.0.1",
    "port": 5432,
    "password": "mypostgres"
}


class Employed(Model):
    id = Model.Id(default=Functions.UUID, primary_key=True, unique=True)
    name = Model.varchar(size=50)
    lastname = Model.varchar(size=50, null=True)
    email = Model.varchar(size=40, unique=True)
    gender = Model.varchar(size=10)
    salary = Model.varchar(size=20)

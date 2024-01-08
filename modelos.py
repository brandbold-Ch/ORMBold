from models.model import Model
from core.db.models import Varchar, UUID, Serial


class Employed(Model):
    id_user = UUID(primary_key=True, auto=True)
    name = Varchar(size=50)
    lastname = Varchar(size=50)
    email = Varchar(size=40)
    gender = Varchar(size=10)
    salary = Varchar(size=20)
    role = Varchar(size=40, default='Worker')

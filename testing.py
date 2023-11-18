from models.model import Model
from utilities.sql_types import Functions
from analyze.reflection import Reflect


class Employed(Model):
    id = Model.setId(function=Functions.AUTOINCREMENT, primary_key=True, unique=True)
    name = Model.varchar(size=50)
    lastname = Model.varchar(size=50, unique=True, null=True)
    email = Model.varchar(size=40, unique=True)
    gender = Model.varchar(size=10)
    salary = Model.varchar(size=20)


if __name__ == '__main__':
    test = Employed()

    test.insert_values(
        name='Jeremy Alexet',
        lastname='De la Rosa Cárdenas',
        email='jeremy@gmail.com',
        gender='Masculino',
        salary='13000'
    )


    #test.delete(
    #    email='jeremy@gmail.com'
    #)

    orm = Reflect(test)

from modelos import Employed
from core.introspection.reflection import Reflect


DATABASE_CONFIG = {
    "engine": "postgres",
    "user": "postgres",
    "dbname": "postgres",
    "host": "127.0.0.1",
    "port": 5432,
    "password": "mypostgres"
}

if __name__ == '__main__':
    test = Employed()

    """
    test.insert_values(
        name="Raul Jose",
        lastname="Escobar de Leon",
        email="jose@gmail.com",
        gender="Masculino",
        salary="3000"
    )
    """

    test.name = 'Brandon Jared'
    test.lastname = 'Molina Vazquez'

    test.save()

    print(test.name)
    print(test.lastname)
    print(test.id_user)

    orm = Reflect()
    orm.add_object(test)
    orm.init()


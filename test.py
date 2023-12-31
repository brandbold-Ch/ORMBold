from modelos import Employed
from analyze.reflection import Reflect

if __name__ == '__main__':
    test = Employed()

    test.insert_values(
        name="Culo",
        lastname="Molina Vazquez",
        email="culotdse@gmail.com",
        gender="Masculino",
        salary="24500"
    )

    test.delete(
        name='culito'
    )

    orm = Reflect()
    orm.add_object(test)
    orm.execute_operations()

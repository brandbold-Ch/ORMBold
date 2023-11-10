from dataclasses import dataclass
from utilities.sentences_sql import SQLGenerator


class Reflect:
    def __init__(self, cls: object) -> None:
        self.cls: cls = cls
        self.init()

    def getNameClass(self) -> str:
        return self.cls.__class__.__name__

    def objFields(self) -> dict:
        return self.cls.__dict__

    def getDeclaredMethods(self) -> None:
        context = self.cls.__class__.__dict__
        for obj in context:
            if type(context[obj]) == type(lambda: None):
                print(str(context[obj]).split(' ')[1].split('.')[1])

    def classFields(self) -> list:
        fields: list = []

        for i in self.cls.__class__.__dict__:
            if not str(i).startswith('__'):
                fields.append((i, eval(f'self.cls.{i}')))

        return fields

    def init(self) -> None:
        fields: list = self.classFields()
        sql: str = ''

        for i in fields:
            sql += f'{str(i[1]).replace("N", i[0], 1)}, \n\t\t\t'

        print(SQLGenerator.create_table(self.getNameClass(), sql))


@dataclass
class Person:
    name = SQLGenerator.varchar(size=50, unique=False, primary_key=True)
    lastname = SQLGenerator.varchar(size=50, unique=True)
    email = SQLGenerator.varchar(size=40, unique=True, primary_key=True)
    gender = SQLGenerator.varchar(size=10, choices=('Masculino', 'Femenino'))


if __name__ == '__main__':
    orm = Reflect(Person())

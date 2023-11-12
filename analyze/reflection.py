from models.model import Model
from utilities.sentences_sql import SQLGenerator


class Reflect:
    def __init__(self, cls: object) -> None:
        self.cls: cls = cls
        self.persistence: SQLGenerator = SQLGenerator('postgres', 'postgres', 'elefante')
        self.init()
        self.runDynamically()

    def getAllMethods(self) -> dict:
        return self.cls.__class__.__dict__

    def getNameClass(self) -> str:
        return self.cls.__class__.__name__.lower()

    def objFields(self) -> dict:
        return self.cls.__dict__

    def getDeclaredMethods(self) -> None:
        context = self.getAllMethods()
        for obj in context:
            if isinstance(type(context[obj]), type(lambda: None)):
                print(str(context[obj]).split(' ')[1].split('.')[1])

    def classFields(self) -> list:
        fields: list = []

        for i in self.getAllMethods():
            if not str(i).startswith('__'):
                fields.append((i, eval(f'self.cls.{i}')))

        return fields

    def init(self) -> None:
        fields: list = self.classFields()
        sql: str = ''

        for i, j in enumerate(fields):
            sql += f'{str(j[1]).replace("V", j[0], 1)}{", " if len(fields) - i  > 1 else ""}'

        self.persistence.execute(
            SQLGenerator.create_table(self.getNameClass(), sql)
        )

    def runDynamically(self):
        for method in self.objFields().get('called'):
            match method[0]:
                case 'insert_values':
                    self.persistence.execute(
                        SQLGenerator.insert(self.getNameClass(), **method[1])
                    )
                    break


class Employed(Model):
    name = Model.varchar(size=50)
    lastname = Model.varchar(size=50, unique=True)
    email = Model.varchar(size=40, unique=True, primary_key=True)
    gender = Model.varchar(size=10)
    salary = Model.varchar(size=20)


if __name__ == '__main__':
    test = Employed()
    test.insert_values(
        name='Pablo Julián',
        lastname='Garay de León',
        email='pablo@gmail.com',
        gender='Men',
        salary='1500'
    )
    orm = Reflect(test)

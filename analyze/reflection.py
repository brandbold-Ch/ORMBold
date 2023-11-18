from utilities.sentences_sql import SQLGenerator
from typing import List, Tuple


class Reflect:
    def __init__(self, cls: object) -> None:
        self.cls: cls = cls
        self.dialect: SQLGenerator = SQLGenerator('postgres', 'postgres', 'elefante')
        self.init()
        self.run_dynamically()

    def get_all_methods(self) -> dict:
        return self.cls.__class__.__dict__

    def get_name_class(self) -> str:
        return self.cls.__class__.__name__.lower()

    def obj_fields(self) -> dict:
        return self.cls.__dict__

    def get_declared_methods(self) -> None:
        context = self.get_all_methods()
        for obj in context:
            if isinstance(type(context[obj]), type(lambda: None)):
                print(str(context[obj]).split(' ')[1].split('.')[1])

    def class_fields(self) -> List[Tuple[str, str]]:
        fields: List[Tuple[str, str]] = []

        for i in self.get_all_methods():
            if not str(i).startswith('__' and '_'):
                fields.append((i, eval(f'self.cls.{i}')))

        return fields

    def init(self) -> None:
        self.dialect.execute(
            self.dialect.create_table(self.get_name_class(), self.class_fields())
        )

    def run_dynamically(self) -> None:
        for method in self.obj_fields().get('_Model__called'):
            match method[0]:

                case 'insert_values':
                    self.dialect.execute(
                        self.dialect.insert(self.get_name_class(), **method[1])
                    )
                    break

                case 'delete':
                    self.dialect.execute(
                        self.dialect.delete(self.get_name_class(), **method[1])
                    )
                    break

                case 'all':
                    self.dialect.execute(
                        self.dialect.all(self.get_name_class(), method[1])
                    )
                    break
                    
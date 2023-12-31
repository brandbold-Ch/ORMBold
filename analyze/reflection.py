from utilities.sentences_sql import PostgresSQLGenerator
from parser_config.read_config import ConfigEngine
from typing import List, Tuple, TypeVar

T = TypeVar('T')


class Reflect:
    syntax: T = None
    object_context: T = None
    pending_objects: List[T] = []

    def __init__(self) -> None:
        match ConfigEngine.get_config_parsed().get('engine'):

            case 'postgres':
                del ConfigEngine.get_config_parsed()["engine"]
                Reflect.syntax = PostgresSQLGenerator(
                    **ConfigEngine.get_config_parsed()
                )

            case 'mysql':
                del ConfigEngine.get_config_parsed()["engine"]

            case _:
                raise ValueError('Engine not supported')

    def add_object(self, obj: T) -> None:
        self.pending_objects.append(obj)

    @classmethod
    def get_all_methods(cls) -> dict:
        return cls.object_context.__class__.__dict__

    @classmethod
    def get_name_class(cls) -> str:
        return cls.object_context.__class__.__name__.lower()

    @classmethod
    def obj_fields(cls) -> dict:
        return cls.object_context.__dict__

    @classmethod
    def class_fields(cls) -> List[Tuple[str, str]]:
        fields: List[Tuple[str, str]] = []

        for i in cls.get_all_methods():
            if not str(i).startswith('__' and '_'):
                fields.append((i, eval(f'cls.object_context.{i}')))  # this line not like

        return fields

    @classmethod
    def execute_operations(cls) -> None:
        for model in cls.pending_objects:
            cls.object_context = model
            cls.__init()

    @classmethod
    def __init(cls):
        cls.create_model()
        cls.run_operations()

    @classmethod
    def create_model(cls) -> None:
        cls.syntax.execute_normal(
            cls.syntax.create_table(cls.get_name_class(), cls.class_fields())
        )

    @classmethod
    def run_operations(cls) -> None:
        for method in cls.obj_fields().get('_Model__pending'):

            if method[0] == 'insert_values':
                cls.syntax.execute_normal(
                    cls.syntax.insert_into(cls.get_name_class(), **method[1])
                )

            elif method[0] == 'delete':
                cls.syntax.execute_normal(
                    cls.syntax.delete(cls.get_name_class(), **method[1])
                )

            elif method[0] == 'all':
                cls.syntax.execute_extra(
                    cls.syntax.select(cls.get_name_class(), method[1])
                )

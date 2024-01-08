from utils.sql_generator.postgres_generator import PostgresSQLGenerator
from utils.parser_config.read_config import ConfigEngine
from utils.languajes.postgres.dml import DML
from utils.languajes.postgres.ddl import DDL
from utils.languajes.postgres.dql import DQL
from typing import List, Tuple, TypeVar

T = TypeVar('T')
E = TypeVar('E')


class Reflect:
    sql_syntax: T = None
    object_context: T = None
    pending_objects: List[E] = []

    def __init__(self) -> None:
        match ConfigEngine.get_config_parsed().get('engine'):

            case 'postgres':
                del ConfigEngine.get_config_parsed()["engine"]
                Reflect.sql_syntax = PostgresSQLGenerator(
                    **ConfigEngine.get_config_parsed()
                )

            case 'mysql':
                del ConfigEngine.get_config_parsed()["engine"]

            case _:
                raise ValueError('Engine not supported')

    def add_object(self, obj: E) -> None:
        self.pending_objects.append(obj)

    @classmethod
    def get_all_attr(cls) -> dict:
        return cls.object_context.__class__.__dict__

    @classmethod
    def get_name_class(cls) -> str:
        return cls.object_context.__class__.__name__.lower()

    @classmethod
    def objects_queries(cls) -> dict:
        return cls.object_context.__dict__

    @classmethod
    def class_fields(cls) -> List[Tuple]:
        fields: List[Tuple] = []

        for i in cls.get_all_attr():
            if not str(i).startswith(('__', '_')):
                fields.append((i, getattr(cls.object_context, i)))

        return fields

    @classmethod
    def init(cls) -> None:
        for model in cls.pending_objects:
            cls.object_context = model
            cls.create_model()
            cls.run_queries()

    @classmethod
    def create_model(cls) -> None:
        cls.sql_syntax.execute_normal(
            DDL.create_table(cls.get_name_class(), cls.class_fields())
        )

    @classmethod
    def run_queries(cls) -> None:
        for method in cls.objects_queries().get('_Model__pending_queries'):

            if method[0] == 'insert_values':
                cls.sql_syntax.execute_normal(
                    DML.insert(cls.get_name_class(), **method[1])
                )

            elif method[0] == 'delete':
                cls.sql_syntax.execute_normal(
                    DML.delete(cls.get_name_class(), **method[1])
                )

            elif method[0] == 'get':
                record: List[Tuple] = cls.sql_syntax.execute_extra(
                    DQL.select(cls.get_name_class(), **method[1])
                )

                if not record:
                    raise ValueError('Not found record')

                for i, j in enumerate(cls.class_fields()):
                    setattr(cls.object_context, j[0], record[0][i])

            elif method[0] == 'all':
                cls.sql_syntax.execute_extra(
                    DQL.select(cls.get_name_class(), method[1], all_records=True)
                )

            elif method[0] == 'save':
                print(cls.class_fields())
                print("Holi")
                cls.sql_syntax.execute_normal(
                    DML.update(cls.get_name_class(), **method[1])
                )

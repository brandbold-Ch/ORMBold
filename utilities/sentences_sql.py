from utilities.sql_types import Types
from psycopg2.extensions import connection
from languajes.postgres.DML.dml import DML
from languajes.postgres.DDL.ddl import DDL
from connection.postgres.postgres_connection import PostgresConnection
from typing import List, Tuple, Any


class PostgresSQLGenerator(Types, DML, DDL, PostgresConnection):

    def __init__(self, dbname: str, user: str, password: str, host: str, port: int):
        Types.__init__(self)
        DML.__init__(self)
        PostgresConnection.__init__(self, dbname, user, password, host, port)

    def connection(self) -> connection:
        return super().connection()

    def execute_normal(self, sentence_sql: str) -> None:
        super().execute_normal(sentence_sql)

    def execute_extra(self, sentence_sql: str) -> List[Tuple[Any, ...]]:
        return super().execute_extra(sentence_sql)

    def update(self, table: str, **kwargs) -> str:
        pass

    def select(self, table: str, order_by: str = None) -> str:
        return super().select(table, order_by)

    def create_table(self, table_name: str, fields: List[Tuple[str, str]]) -> str:
        return super().create_table(table_name, fields)

    def insert_into(self, table, **kwargs) -> str:
        return super().insert_into(table, **kwargs)

    def delete(self, table, **kwargs) -> str:
        return super().delete(table, **kwargs)

    def integer(self):
        pass

    def date(self):
        pass

    def varchar(self, size: int, null: bool = True, unique: bool = False, primary_key: bool = False) -> str:
        return super().varchar(size, null, unique, primary_key)

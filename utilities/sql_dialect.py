from bases.crud import CrudOperations
from typing import List, Tuple


class SqlDialect(CrudOperations):

    def __init__(self):
        pass

    @staticmethod
    def create_table(table_name: str, fields: List[Tuple[str, str]]) -> str:
        sql: str = ''

        for i, j in enumerate(fields):
            sql += f'{str(j[1]).replace("V", j[0], 1)}{", " if len(fields) - i > 1 else ""}'

        return f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {sql}
            );"""

    @staticmethod
    def insert(table, **kwargs) -> str:
        values: list = list(map(lambda x: f"'{x}'", list(kwargs.values())))

        return f"""
            INSERT INTO {table} ({', '.join(list(kwargs))})
            VALUES ({', '.join(values)}
            );"""

    @staticmethod
    def delete(table, **kwargs) -> str:
        return f"""
            DELETE FROM {table}
            WHERE {list(kwargs.keys())[0]}={f"'{list(kwargs.values())[0]}'"};
        """

    @staticmethod
    def find(table: str, **kwargs) -> str:
        pass

    @staticmethod
    def filter(table: str, **kwargs) -> str:
        pass

    @staticmethod
    def all(table: str, order_by: str = None) -> str:
        return f"""
            SELECT *FROM {table};
        """

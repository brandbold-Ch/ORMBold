import psycopg2
from utilities.sql_types import Types
from utilities.sql_dialect import SqlDialect
from typing import List, Tuple


class SQLGenerator(Types, SqlDialect):

    def __init__(self, dbname: str = None, user: str = None, password: str = None, host: str = '127.0.0.1',
                 port: int = 5432) -> None:
        Types.__init__(self)
        SqlDialect.__init__(self)
        self.__dbname: str = dbname
        self.__user: str = user
        self.__password: str = password
        self.__host: str = host
        self.__port: int = port

    def __connection(self) -> psycopg2:
        conn: psycopg2 = psycopg2.connect(
            dbname=self.__dbname,
            user=self.__user,
            password=self.__password,
            host=self.__host,
            port=self.__port
        )
        return conn

    def execute(self, sentence):
        try:
            connection: psycopg2 = self.__connection()
            cursor: psycopg2 = connection.cursor()
            cursor.execute(sentence)
            connection.commit()
            cursor.close()
            connection.close()

            print("Finished")
        except Exception as e:
            print(e)

    def find(self, table: str, **kwargs) -> str:
        pass

    def filter(self, table: str, **kwargs) -> str:
        pass

    def all(self, table: str, order_by: str = None) -> str:
        pass

    def create_table(self, table_name: str, fields: List[Tuple[str, str]]) -> str:
        return super().create_table(table_name, fields)

    def insert(self, table, **kwargs) -> str:
        return super().insert(table, **kwargs)

    def delete(self, table, **kwargs) -> str:
        return super().delete(table, **kwargs)

    def integer(self):
        pass

    def date(self):
        pass

    def varchar(self, size: int, null: bool = True, unique: bool = False, primary_key: bool = False) -> str:
        return super().varchar(size, null, unique, primary_key)

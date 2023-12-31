from psycopg2.extensions import connection, cursor
from typing import List, Tuple, Any
import psycopg2


class PostgresConnection:

    def __init__(self, dbname: str, user: str, password: str, host: str, port: int) -> None:
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connection(self) -> connection:
        connect: connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        return connect

    def execute_normal(self, sentence_sql: str) -> None:
        link: connection = self.connection()
        executor: cursor = link.cursor()
        executor.execute(sentence_sql)
        link.commit()
        executor.close()
        link.close()

    def execute_extra(self, sentence_sql: str) -> List[Tuple[Any, ...]]:
        link: connection = self.connection()
        executor: cursor = link.cursor()
        executor.execute(sentence_sql)
        data: List[Tuple[Any, ...]] = executor.fetchall()
        link.commit()
        executor.close()
        link.close()

        return data

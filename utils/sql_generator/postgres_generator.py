from utils.connection.postgres_connection import PostgresConnection
from psycopg2.extensions import connection
from typing import List, Tuple


class PostgresSQLGenerator(PostgresConnection):

    def __init__(self, dbname: str, user: str, password: str, host: str, port: int) -> None:
        super().__init__(dbname, user, password, host, port)

    def connection(self) -> connection:
        return super().connection()

    def execute_normal(self, sentence_sql: str) -> None:
        super().execute_normal(sentence_sql)

    def execute_extra(self, sentence_sql: str) -> List[Tuple]:
        return super().execute_extra(sentence_sql)

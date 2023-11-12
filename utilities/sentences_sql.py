import psycopg2


class SQLGenerator:

    def __init__(self, dbname: str = None, user: str = None, password: str = None, host: str = '127.0.0.1',
                 port: int = 5432) -> None:
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

    @staticmethod
    def create_table(table_name: str, fields: str):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {fields}
        );"""
        return sql

    @staticmethod
    def insert(table, **kwargs) -> str:
        values: list = list(map(lambda x: f"'{x}'", list(kwargs.values())))

        return f"""
        INSERT INTO {table} ({', '.join(list(kwargs))})
        VALUES ({', '.join(values)});
        """

    @staticmethod
    def integer():
        pass

    @staticmethod
    def date():
        pass

    @staticmethod
    def varchar(size: int, null: bool = True, unique: bool = False, charset: str = None,
                choices: tuple = None,
                primary_key: bool = False) -> str:

        constrains: list = [
            'V',
            f'VARCHAR({size})',
            'NULL' if null else 'NOT NULL',
            'UNIQUE' if unique else '',
            'PRIMARY KEY' if primary_key else ''
        ]

        constrains = list(filter(lambda x: x if x != '' else None, constrains))

        return ' '.join(constrains)

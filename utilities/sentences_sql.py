import psycopg2


class SQLGenerator:
    def __init__(self, dbname: str, user: str, password: str, host: str = '127.0.0.1', port: int = 5432) -> None:
        self.dbname: str = dbname
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.port: int = port

    @classmethod
    def connection(cls, *args) -> psycopg2:
        conn: psycopg2 = psycopg2.connect(
            dbname=cls.dbname,
            user=cls.user,
            password=cls.password,
            host=cls.host,
            port=cls.port
        )
        return conn

    @property
    def dbname(self) -> str:
        return self.dbname

    @property
    def user(self) -> str:
        return self.user

    @property
    def password(self) -> str:
        return self.password

    @property
    def host(self) -> str:
        return self.host

    @property
    def port(self) -> int:
        return self.port

    @dbname.setter
    def dbname(self, db: str):
        self.dbname = db

    @user.setter
    def user(self, user: str):
        self.user = user

    @password.setter
    def password(self, password: str):
        self.password = password

    @host.setter
    def host(self, host: str):
        self.host = host

    @port.setter
    def port(self, port: str):
        self.port = port

    @staticmethod
    def create_table(table_name: str, fields: str):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {fields}
        );"""
        return sql

    @staticmethod
    def varchar(size: int, null: bool = True, unique: bool = False, charset: str = None,
                choices: tuple = None,
                primary_key: bool = False) -> str:

        constrains: list = []
        sql: str = 'N'

        if size:
            constrains.append(f'VARCHAR({size})')
        else:
            raise Exception('Se necesita el tamaño del campo')

        if null:
            constrains.append('NULL')
        else:
            constrains.append('NOT NULL')

        if unique:
            constrains.append('UNIQUE')
        else:
            pass

        if choices is not None:
            constrains.append(f'ENUM{choices}')
        else:
            pass

        if primary_key:
            constrains.append('PRIMARY KEY')
        else:
            pass

        for options in constrains:
            sql += f' {options}'

        return sql
    
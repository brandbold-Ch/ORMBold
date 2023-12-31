from bases.sql.type_data.types import BaseTypes


class Functions:
    AUTOINCREMENT: str = 'SERIAL'
    UUID: str = 'gen_random_uuid()'


class Types(BaseTypes):

    def __init__(self):
        pass

    @staticmethod
    def Id(default: str, unique: bool = False, primary_key: bool = False) -> str:

        if Functions.UUID or default or Functions.AUTOINCREMENT:

            constrains: list = [
                'V',
                f'UUID DEFAULT {Functions.UUID}' if default == Functions.UUID else Functions.AUTOINCREMENT,
                'UNIQUE' if unique else '',
                'PRIMARY KEY' if primary_key else ''
            ]
            constrains = list(filter(lambda x: x if x != '' else None, constrains))

            return ' '.join(constrains)

        else:
            raise Exception('Invalid sql methods')

    @staticmethod
    def integer():
        pass

    @staticmethod
    def date():
        pass

    @staticmethod
    def varchar(size: int, null: bool = True, unique: bool = False, primary_key: bool = False) -> str:
        constrains: list = [
            'V',
            f'VARCHAR({size})',
            'NULL' if null else 'NOT NULL',
            'UNIQUE' if unique else '',
            'PRIMARY KEY' if primary_key else ''
        ]
        constrains = list(filter(lambda x: x if x != '' else None, constrains))

        return ' '.join(constrains)

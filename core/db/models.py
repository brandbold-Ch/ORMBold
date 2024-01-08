from typing import List
from datetime import date


class Field:
    def __init__(self, null: bool = True, unique: bool = False, primary_key: bool = False,
                 blank: bool = True) -> None:
        self.null = null
        self.blank = blank
        self.unique = unique
        self.primary_key = primary_key

    def validate(self) -> None:

        values: list = [
            self.null.__class__,
            self.blank.__class__,
            self.unique.__class__,
            self.primary_key.__class__
        ]

        if values.count(bool) == 4:
            pass
        else:
            raise TypeError('Invalid type data options')

    def constrains(self) -> List[str]:
        pass

    def clean_constrains(self, constrains) -> List[str]:
        return list(filter(lambda x: x if x != '' else None, constrains))

    def create_sql(self, constrains: List[str]) -> str:
        return ' '.join(constrains)


class Varchar(Field):
    def __init__(self, size: int, default: str = None, null: bool = True, unique: bool = False,
                 primary_key: bool = False, blank: bool = True) -> None:
        super().__init__(null, unique, primary_key, blank)
        self.default = default
        self.size = size
        super().validate()

    def validate(self) -> None:
        if isinstance(self.size, int):
            if (0 <= self.size <= 65535) is False:
                raise ValueError('Limit exceeded')
        else:
            raise TypeError('Invalid type data')

    def constrains(self) -> List[str]:
        simple_assignment: str = f"VARCHAR({self.size})"
        default_value: str = f"{simple_assignment} DEFAULT '{self.default}'"

        return super().clean_constrains([
            'K',
            simple_assignment if self.default is None else default_value,
            'NULL' if self.null else 'NOT NULL',
            'UNIQUE' if self.unique else '',
            'PRIMARY KEY' if self.primary_key else ''
        ])

    def __str__(self) -> str:
        return super().create_sql(self.constrains())


class Integer:

    def __init__(self) -> None:
        pass


class Float:

    def __init__(self) -> None:
        pass


class Text(Field):
    def __init__(self, default: str = None, null: bool = True, unique: bool = False, primary_key: bool = False,
                 blank: bool = True) -> None:
        super().__init__(null, unique, primary_key, blank)
        self.default = default


class UUID(Field):
    def __init__(self, auto: bool = False, null: bool = True, unique: bool = False, primary_key: bool = False,
                 blank: bool = True) -> None:
        super().__init__(null, unique, primary_key, blank)
        self.auto = auto
        super().validate()

    def validate(self) -> None:
        if isinstance(self.auto, bool) is False:
            raise TypeError('Invalid type data')

    def constrains(self) -> List[str]:
        return super().clean_constrains([
            'K',
            f'UUID DEFAULT gen_random_uuid()' if self.auto else 'UUID',
            'NULL' if self.null else 'NOT NULL',
            'UNIQUE' if self.unique else '',
            'PRIMARY KEY' if self.primary_key else ''
        ])

    def __str__(self):
        return super().create_sql(self.constrains())


class Serial(Field):
    def __init__(self, null: bool = True, unique: bool = False, primary_key: bool = False,
                 blank: bool = True) -> None:
        super().__init__(null, unique, primary_key, blank)
        super().validate()

    def constrains(self) -> List[str]:
        return super().clean_constrains([
            'K',
            'SERIAL',
            'UNIQUE' if self.unique else '',
            'PRIMARY KEY' if self.primary_key else ''
        ])

    def __str__(self):
        return super().create_sql(self.constrains())


class Date(Field):
    def __init__(self, null: bool = True, unique: bool = False, primary_key: bool = False,
                 blank: bool = True) -> None:
        super().__init__(null, unique, primary_key, blank)

import json
from typing import List


class ConfigEngine:

    config = {}

    @classmethod
    def read_config_object(cls, url_file: str) -> None:

        with open(url_file, 'r', encoding='utf-8') as py:
            array_string: List[str] = py.readlines()

            start: int = next((i for i, j in enumerate(array_string) if j.startswith('DATABASE_CONFIG')), None)
            end: int = next((i for i, j in enumerate(array_string) if j.startswith('}\n')), None)

            if start is not None and end is not None:
                cls.config = json.loads(''.join(array_string[start:end + 1])[18:])

            else:
                raise ValueError('Database configuration not found')

    @classmethod
    def get_config_parsed(cls) -> dict:
        return cls.config

from utils.parser_config.read_config import ConfigEngine
from typing import List, Tuple
import os.path
import sys


class Model:

    def __init__(self):
        self.__pending_queries: List[Tuple] = []
        ConfigEngine.read_config_object(os.path.abspath(sys.argv[0]))

    def insert_values(self, **kwargs) -> None:
        self.__pending_queries.append(('insert_values', kwargs))

    def delete(self, **kwargs) -> None:
        self.__pending_queries.append(('delete', kwargs))

    def get(self, **kwargs) -> None:
        self.__pending_queries.append(('get', kwargs))

    def all(self, order_by: str = None) -> None:
        self.__pending_queries.append(('all', order_by))

    def save(self) -> None:
        self.__pending_queries.append(('save', {}))

from parser_config.read_config import ConfigEngine
from utilities.sql_types import Types
import os.path
import inspect
import sys


class Model(Types):

    def __init__(self):
        super().__init__()
        self.__pending: list = []
        ConfigEngine.read_config_object(os.path.abspath(sys.argv[0]))
        print(inspect.getmembers(self))

    def insert_values(self, **kwargs) -> None:
        self.__pending.append(('insert_values', kwargs))

    def delete(self, **kwargs) -> None:
        self.__pending.append(('delete', kwargs))

    def get(self, **kwargs) -> None:
        self.__pending.append(('get', kwargs))

    def all(self, order_by: str = None):
        self.__pending.append(('all', order_by))

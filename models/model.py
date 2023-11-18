from utilities.sql_types import Types


class Model(Types):

    def __init__(self):
        super().__init__()
        self.__called: list = []

    def insert_values(self, **kwargs) -> None:
        self.__called.append(('insert_values', kwargs))

    def delete(self, **kwargs) -> None:
        self.__called.append(('delete', kwargs))

    def get(self, **kwargs) -> None:
        self.__called.append(('get', kwargs))

    def all(self, order_by: str = None):
        self.__called.append(('all', order_by))

from abc import ABC, abstractmethod


class CrudOperations(ABC):

    @staticmethod
    @abstractmethod
    def insert(table: str, **kwargs) -> str:
        pass

    @staticmethod
    @abstractmethod
    def delete(table: str, **kwargs) -> str:
        pass

    @staticmethod
    @abstractmethod
    def find(table: str, **kwargs) -> str:
        pass

    @staticmethod
    @abstractmethod
    def filter(table: str, **kwargs) -> str:
        pass

    @staticmethod
    @abstractmethod
    def all(table: str, order_by: str = None) -> str:
        pass

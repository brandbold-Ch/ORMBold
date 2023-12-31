from abc import ABC, abstractmethod


class DMLBases(ABC):

    @staticmethod
    @abstractmethod
    def insert_into(table: str, **kwargs) -> str:
        pass

    @staticmethod
    @abstractmethod
    def delete(table: str, **kwargs) -> str:
        pass

    @staticmethod
    @abstractmethod
    def update(table: str, **kwargs) -> str:
        pass

    @staticmethod
    @abstractmethod
    def select(table: str, order_by: str = None) -> str:
        pass

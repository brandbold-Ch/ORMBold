from abc import ABC, abstractmethod


class DMLBases(ABC):

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
    def update(table: str, **kwargs) -> str:
        pass

from abc import ABC, abstractmethod


class BaseTypes(ABC):

    @staticmethod
    @abstractmethod
    def setId(function: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def integer() -> str:
        pass

    @staticmethod
    @abstractmethod
    def date() -> str:
        pass

    @staticmethod
    @abstractmethod
    def varchar(size: int, null: bool = True, unique: bool = False, primary_key: bool = False) -> str:
        pass

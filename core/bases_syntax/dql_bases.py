from abc import ABC, abstractmethod


class DQLBases(ABC):

    @staticmethod
    @abstractmethod
    def select(table: str, order_by: str = None, all_records: bool = False, **kwargs) -> str:
        pass

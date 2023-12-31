from abc import ABC, abstractmethod
from typing import List, Tuple


class DDLBases(ABC):

    @staticmethod
    @abstractmethod
    def create_table(table_name: str, fields: List[Tuple[str, str]]) -> str:
        pass

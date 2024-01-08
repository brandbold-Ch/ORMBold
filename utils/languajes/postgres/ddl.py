from core.bases_syntax.ddl_bases import DDLBases
from typing import List, Tuple


class DDL(DDLBases):

    @staticmethod
    def create_table(table_name: str, fields: List[Tuple[str, str]]) -> str:
        sql: str = ''

        for i, j in enumerate(fields):
            sql += f'{str(j[1]).replace("K", j[0], 1)}{", " if (len(fields) - i) > 1 else ""}'

        return f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {sql}
            );
        """

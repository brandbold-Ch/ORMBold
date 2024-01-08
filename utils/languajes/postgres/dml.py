from core.bases_syntax.dml_bases import DMLBases


class DML(DMLBases):

    @staticmethod
    def insert(table, **kwargs) -> str:
        values: list = [f"'{x}'" for x in kwargs.values()]

        return f"""
            INSERT INTO {table} ({', '.join(list(kwargs))})
            VALUES ({', '.join(values)}
            );
        """

    @staticmethod
    def delete(table, **kwargs) -> str:
        return f"""
            DELETE FROM {table}
            WHERE {list(kwargs.keys())[0]}={f"'{list(kwargs.values())[0]}'"};
        """

    @staticmethod
    def update(table: str, **kwargs) -> str:
        return f"""
            UPDATE {table} SET {kwargs}
            WHERE {2};
        """

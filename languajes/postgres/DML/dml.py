from bases.sql.sentences.DML.dml_bases import DMLBases


class DML(DMLBases):

    @staticmethod
    def insert_into(table, **kwargs) -> str:
        values: list = list(map(lambda x: f"'{x}'", list(kwargs.values())))

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
        pass

    @staticmethod
    def select(table: str, order_by: str = None) -> str:
        return f"""
            SELECT *FROM {table};
        """

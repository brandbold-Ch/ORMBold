from core.bases_syntax.dql_bases import DQLBases


class DQL(DQLBases):

    @staticmethod
    def select(table: str, order_by: str = None, all_records: bool = False, **kwargs) -> str:
        if all_records:
            return f"""
                SELECT *FROM {table};
            """
        else:
            return f"""
                SELECT *FROM {table}
                WHERE {list(kwargs.keys())[0]}={f"'{list(kwargs.values())[0]}'"};
            """

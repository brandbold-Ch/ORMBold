from utilities.sentences_sql import SQLGenerator


class Model(SQLGenerator):

    def __init__(self):
        super().__init__()
        self.called: list = []

    def insert_values(self, **kwargs) -> None:
        self.called.append(('insert_values', kwargs))

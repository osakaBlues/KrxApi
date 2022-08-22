class SchemaError(Exception):
    pass


class WrongSchemaName(Exception):
    def __init__(self, schema):
        super().__init__(f"{schema} is not defined")


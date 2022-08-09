class SchemaError(Exception):
    def __init__(self, s: str):
        super().__init__(f"schemas 파일의 {s}를 확인해 보세요")


from KrxApi.payload import Payload
from KrxApi.resources.schemas import schemas


class SchemaError(Exception):
    def __init__(self, s: str):
        super().__init__(f"schemas 파일의 {s}를 확인해 보세요")


class PayloadBuilder:
    __slots__ = ['_payload']

    def __init__(self, schema_key: str):
        self._payload: Payload = Payload()
        schema: dict = schemas[schema_key]
        for k, v in schema.items():
            if type(v) != dict:
                raise SchemaError(k)
            value = v.get("value", None)
            setattr(self._payload, k, value)

    def build(self) -> Payload:
        return self._payload

    def set_attribute(self, key: str, value: any) -> 'PayloadBuilder':
        if not hasattr(self._payload, key):
            raise SchemaError(key)
        setattr(self._payload, key, value)
        return self

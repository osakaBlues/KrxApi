from KrxApi.payload import Payload
from KrxApi.resources.schemas import Attr, validate_schema
from KrxApi.resources.SchemaError import SchemaError


class PayloadBuilder:
    __slots__ = ['_payload']

    def __init__(self, schema: dict):
        self._payload: Payload = Payload()
        for k, v in schema.items():
            setattr(self._payload, k, v.get(Attr.value))

    def build(self) -> Payload:
        return self._payload

    def set_attribute(self, key: str, value: any) -> 'PayloadBuilder':
        if not hasattr(self._payload, key):
            raise SchemaError(key)
        setattr(self._payload, key, value)
        return self

    def set_attributes(self, attributes: dict) -> 'PayloadBuilder':
        for k, v in attributes.items():
            self.set_attribute(k, v)
        return self


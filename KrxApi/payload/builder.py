from KrxApi.payload import Payload
from KrxApi.resources.schemas import Attr
from KrxApi.resources.SchemaError import SchemaError


class PayloadBuilder:
    __slots__ = ['_payload', '_schema']

    def __init__(self, schema: dict):
        self._payload: Payload = Payload()
        for k, v in schema.items():
            setattr(self._payload, k, v.get(Attr.value))
        self._schema: dict = schema

    def build(self) -> Payload:
        for k, v in self._schema.items():
            required_attr = v.get(Attr.required)
            if required_attr is True and getattr(self._payload, k) is None:
                raise SchemaError
        return self._payload

    def set_attribute(self, key: str, value: any) -> 'PayloadBuilder':
        if not hasattr(self._payload, key):
            raise SchemaError(key)
        attrs = self._schema.get(key)
        if not attrs.get(Attr.mutable, True):
            raise SchemaError(key)
        setattr(self._payload, key, value)
        return self

    def set_attributes(self, attributes: dict) -> 'PayloadBuilder':
        for k, v in attributes.items():
            self.set_attribute(k, v)
        return self


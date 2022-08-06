from KrxApi.serializer import Deserializer, DeserializeError
from KrxApi.KrxResponse import KrxResponse
from KrxApi.connection import Connection


class Command:
    __slots__ = ['deserializer', 'connection']

    def __init__(self, connection: Connection):
        self.deserializer: Deserializer = Deserializer()
        self.connection: Connection = connection

    def execute(self) -> KrxResponse:
        if self.connection is None:
            raise NotImplementedError
        try:
            result = self.deserializer.deserialize(self.connection.get_data())
        except DeserializeError:
            raise ConnectionError
        return KrxResponse(result)

    def get_result(self):
        if self.connection is None:
            raise NotImplementedError
        try:
            result = self.deserializer.deserialize(self.connection.get_data())
        except DeserializeError:
            raise ConnectionError
        return result


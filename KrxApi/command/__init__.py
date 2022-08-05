from KrxApi.serializer import Deserializer, DeserializeError
from KrxApi.KrxResponse import KrxResponse
from KrxApi.connection import Connection


class Command:
    __slots__ = ['deserializer', 'connection', 'krxResponse']

    def __init__(self, connection: Connection, **kwargs):
        self.deserializer: Deserializer = Deserializer()
        self.connection: Connection = connection
        self.krxResponse: KrxResponse = KrxResponse()

    def execute(self) -> KrxResponse:
        if self.connection is None:
            raise NotImplementedError
        try:
            result = self.deserializer.deserialize(self.connection.get_data())
        except DeserializeError:
            raise ConnectionError
        return self.krxResponse.get_data(result)

from KrxApi.resources import *
from KrxApi.serializer import Deserializer
from KrxApi.KrxResponse import KrxResponse
from KrxApi.payload import Payload
from KrxApi.connection import Connection


class Command:
    __slots__ = ['deserializer', 'connection']

    def __init__(self, connection: Connection):
        self.deserializer: Deserializer = Deserializer()
        self.connection: Connection = connection

    def execute(self) -> KrxResponse:
        if self.connection is None:
            raise NotImplementedError
        result = self.deserializer.deserialize(self.connection.get_data())
        return KrxResponse(result)

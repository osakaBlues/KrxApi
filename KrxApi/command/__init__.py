from KrxApi.serializer import Deserializer, DeserializeError
from KrxApi.KrxResponse import KrxResponse
from KrxApi.connection import Connection


class Command:
    """
        Args:
            deserializer (Deserializer): connection을 통해 얻어온 데이터를 deserialize한다.
            connection (Connection): 데이터를 요청하는 객체
    """
    __slots__ = ['deserializer', 'connection']

    def __init__(self, connection: Connection):
        self.deserializer: Deserializer = Deserializer()
        self.connection: Connection = connection

    def execute(self) -> KrxResponse:
        if self.connection is None:
            raise ConnectionError("The Connection is not set")
        try:
            result = self.deserializer.deserialize(self.connection.get_data())
        except DeserializeError:
            raise ConnectionError("Failed to get data from connection")
        return KrxResponse(result)

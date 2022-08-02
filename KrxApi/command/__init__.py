from KrxApi.resources import *
from KrxApi.serializer import Deserializer
from KrxApi.KrxResponse import KrxResponse
from KrxApi.payload import Payload
import requests


class Command:
    deserializer: Deserializer
    payload: Payload
    url: str = None

    def __init__(self, payload):
        self.payload = payload
        self.deserializer = Deserializer()

    def execute(self) -> KrxResponse:
        if self.url is None:
            raise NotImplementedError
        response = requests.get(self.url, params=self.payload.to_dict())
        result = self.deserializer.deserialize(response.text)
        return KrxResponse(result)

class BldCommand(Command):
    url = URLS.STOCK_INFO_CMD
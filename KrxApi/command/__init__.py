from KrxApi.resources import *
from KrxApi.serializer import Deserializer
from KrxApi.KrxResponse import KrxResponse
import requests


class Command:
    deserializer: Deserializer

    def __init__(self, payload):
        self.payload = payload
        self.deserializer = Deserializer()

    def execute(self) -> KrxResponse:
        response = requests.get(URLS.STOCK_INFO_CMD, params=self.payload.to_dict())
        result = self.deserializer.deserialize(response.text)
        return KrxResponse(result)

from ..payload import Payload
from ..resources import URLS
from ..serializer import Deserializer
from ..KrxResponse import KrxResponse
import requests


class Command:
    payload: Payload
    deserializer: Deserializer

    def __init__(self, payload: Payload):
        self.payload = payload
        self.deserializer = Deserializer()

    def execute(self):
        response = requests.get(URLS.STOCK_INFO_CMD, params=self.payload.to_dict())
        result = self.deserializer.deserialize(response.text)
        return KrxResponse(result)

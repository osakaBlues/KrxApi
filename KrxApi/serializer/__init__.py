import json
from json import JSONDecodeError


class DeserializeError(Exception):
    def __init__(self):
        super().__init__()


class Deserializer:
    def deserialize(self, raw_json):
        try:
            result = json.loads(raw_json)
        except JSONDecodeError:
            raise DeserializeError()
        return result


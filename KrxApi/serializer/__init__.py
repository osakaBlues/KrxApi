import json


class Deserializer:
    def deserialize(self, raw_json):
        return json.loads(raw_json)

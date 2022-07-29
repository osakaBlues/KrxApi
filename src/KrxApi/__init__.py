from .command import Command
from .payload import Payload
from .serializer import Deserializer


class Krx:
    def get_all_stocks_price(self):
        pl = Payload()
        cmd = Command(pl)
        deserializer = Deserializer()
        result = cmd.execute()
        return result


__all__ = ["Krx"]

import inspect
from KrxApi.resources import *


class Payload:
    def to_dict(self) -> dict:
        result = {}
        for k in dir(self):
            v = getattr(self, k)
            if not callable(v) and not k.startswith("_") and v is not None:
                result[k] = v
        return result


class PayloadStock(Payload):
    adjStkPrc_check: str = None
    adjStkPrc: str = None
    bld: str = None
    locale: str = LOCALE.KOR
    mktId: str = MARKETS.ALL
    trdDd: str = None
    strtDd: str = None
    endDd: str = None
    share: int = SHARE.ONE
    money: int = MONEY.WON
    csvxls_isNo: bool = False



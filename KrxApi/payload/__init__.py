from KrxApi.resources import *


class Payload:
    __slots__ = []

    def to_dict(self) -> dict:
        result = {}
        for k in dir(self):
            try:
                v = getattr(self, k)
            except AttributeError:
                continue
            if not callable(v) and not k.startswith("_") and v is not None:
                result[k] = v
        return result


class PayloadStock(Payload):
    __slots__ = ['adjStkPrc_check',
                 'adjStkPrc',
                 'bld',
                 'codeNmisuCd_finder_stkisu0_0',
                 'consonant',
                 'isuCd',
                 'isuCd2',
                 'locale',
                 'mktId',
                 'mktsel',
                 'param1isuCd_finder_stkisu0_0',
                 'trdDd',
                 'tboxisuCd_finder_stkisu0_3',
                 'strtDd',
                 'endDd',
                 'share',
                 'searchText',
                 'money',
                 'typeNo',
                 'csvxls_isNo']

    def __init__(self):
        self.locale: str = LOCALE.KOR
        self.mktId: str = MARKETS.ALL
        self.share: int = SHARE.ONE
        self.money: int = MONEY.WON
        self.csvxls_isNo: bool = False



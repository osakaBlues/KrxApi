class Payload:
    _adjStkPrc_check = "Y"
    _adjStkPrc = "2"
    _bld = "dbms/MDC/STAT/standard/MDCSTAT01501"
    _locale = "ko_KR"
    _mktId = "ALL"
    _trdDd = "20220728"
    _strtDd = "20220728"
    _endDd = "20220728"
    _share = "1"
    _money = "1"
    _csvxls_isNo = "false"

    def to_dict(self) -> dict:
        return {}


class PayloadAllStocks(Payload):
    def __init__(self, mktid, trddd, share, money):
        self._mktId = mktid
        self._trdDd = trddd
        self._share = share
        self._money = money

    def to_dict(self):
        return {
            "bld": self._bld,
            "locale": self._locale,
            "mktId": self._mktId,
            "trdDd": self._trdDd,
            "share": self._share,
            "money": self._money,
            "csvxls_isNo": self._csvxls_isNo
        }


class PayloadAllStocksFlRate(Payload):
    def __init__(self, mktid, strtdd, enddd, share, money):
        self._bld = "dbms/MDC/STAT/standard/MDCSTAT01602"
        self._mktId = mktid
        self._strtDd = strtdd
        self._endDd = enddd
        self._share = share
        self._money = money

    def to_dict(self):
        return {
            "bld": self._bld,
            "locale": self._locale,
            "mktId": self._mktId,
            "strtDd": self._strtDd,
            "endDd": self._endDd,
            "adjStkPrc_check": self._adjStkPrc_check,
            "adjStkPrc": self._adjStkPrc,
            "share": self._share,
            "money": self._money,
            "csvxls_isNo": self._csvxls_isNo
        }

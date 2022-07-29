class Payload:
    _bld = "dbms/MDC/STAT/standard/MDCSTAT01501"
    _locale = "ko_KR"
    _mktId = "ALL"
    _trdDd = "20220728"
    _share = "1"
    _money = "1"
    _csvxls_isNo = "false"

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
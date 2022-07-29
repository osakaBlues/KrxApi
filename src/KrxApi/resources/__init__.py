from .constant import Constant


class _URLS(Constant):
    STOCK_INFO_CMD = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'


URLS = _URLS()

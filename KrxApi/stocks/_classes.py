import datetime

from ..command import *
from ..util.get_time import *
from ..connection import *
from ..resources import *
from ..payload.builder import *


class AllStockPrice:
    _parameter_constraints = {
        "mktId": ('ALL', 'SKT', 'KSQ', 'KNX'),
        "trdDd": "%Y%m%d"
    }

    def __init__(self,
                 mktId="ALL",
                 trdDd=get_formatted_date_today()):
        if mktId not in self._parameter_constraints["mktId"]:
            raise ValueError("Invalid market code please check 'mktId'")
        datetime.datetime.strptime(trdDd, self._parameter_constraints["trdDd"])

        self._mktId = mktId
        self._trdDd = trdDd
        self._data = None

    def get(self):
        self._data = Command(
            Connection(
                (PayloadBuilder("all_stock_prices")
                 .set_attribute('mktId', self._mktId)
                 .set_attribute('trdDd', self._trdDd)
                 .build()),
                URLS.STOCK_INFO_CMD)
        ).get_result()

    def data(self,
             full_code=False,
             fluc_rate=False,
             trade_amount=False,
             trade_money=False,
             market_capitalization=False,
             total_stocks=False):
        if self._data is None:
            raise ValueError("Stock data is not loaded yet. Call 'get' with "
                             "appropriate arguments before using this method.")

        from ..DataProcessing import ProcessAllStockPrice

        _process_data = ProcessAllStockPrice(self._data)

        return _process_data.filter(full_code,
                                    fluc_rate,
                                    trade_amount,
                                    trade_money,
                                    market_capitalization,
                                    total_stocks)

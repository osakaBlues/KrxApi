from ..command import *
from ..util.get_time import *
from ..connection import *
from ..resources import *
from ..payload.builder import *
from ..KrxResponse import KrxResponse
import json


class AllStockPrice:
    _parameter_constraints = {
        "mktId": ('ALL', 'SKT', 'KSQ', 'KNX'),
        "trdDd": "%Y%m%d"
    }

    def __init__(self,
                 mktId="ALL",
                 trdDd=get_formatted_date_today()):
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
             market_capitalization=False
             ):
        if self._data is None:
            raise ValueError("Stock data is not loaded yet. Call 'get' with "
                             "appropriate arguments before using this method.")
        return self._data

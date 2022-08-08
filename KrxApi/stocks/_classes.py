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

        from ._names import names_total as nt

        params = {"ISU_SRT_CD": True,
                  "ISU_CD": full_code,
                  "ISU_ABBRV": True,
                  "MKT_NM": True,
                  "SECT_TP_NM": False,
                  "TDD_CLSPRC": True,
                  "FLUC_TP_CD": False,
                  "CMPPREVDD_PRC": True,
                  "FLUC_RT": fluc_rate,
                  "TDD_OPNPRC": False,
                  "TDD_HGPRC": False,
                  "TDD_LWPRC": False,
                  "ACC_TRDVOL": trade_amount,
                  "ACC_TRDVAL": trade_money,
                  "MKTCAP": market_capitalization,
                  "LIST_SHRS": total_stocks,
                  "MKT_ID": False}

        result = []
        names = {}
        for n in params.keys():
            names[n] = nt.get(n)

        for stk in self._data["OutBlock_1"]:
            temp = {}
            for k in params.keys():
                if params.get(k) is True:
                    temp[names.get(k)] = stk.get(k)
            result.append(temp)

        result.append(self._data["CURRENT_DATETIME"])
        return result

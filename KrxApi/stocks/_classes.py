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
        names = {"ISU_SRT_CD": "종목코드",
                 "ISU_CD": "표준종목코드",
                 "ISU_ABBRV": "종목명",
                 "MKT_NM": "시장구분",
                 "SECT_TP_NM": "소속부",
                 "TDD_CLSPRC": "종가",
                 "FLUC_TP_CD": "?",
                 "CMPPREVDD_PRC": "대비",
                 "FLUC_RT": "등락률",
                 "TDD_OPNPRC": "시가",
                 "TDD_HGPRC": "고가",
                 "TDD_LWPRC": "저가",
                 "ACC_TRDVOL": "거래량",
                 "ACC_TRDVAL": "거래대금",
                 "MKTCAP": "시가총액",
                 "LIST_SHRS": "상장주식수",
                 "MKT_ID": "시장코드"}
        result = []

        for stk in self._data["OutBlock_1"]:
            temp = {}
            for k in params.keys():
                if params.get(k) is True:
                    temp[names.get(k)] = stk.get(k)
            result.append(temp)

        result.append(self._data["CURRENT_DATETIME"])
        return result

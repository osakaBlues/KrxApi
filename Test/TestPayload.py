import unittest

from KrxApi.payload import Payload
from KrxApi.payload.builder import PayloadBuilder
from KrxApi.resources import *


class TestPayload(unittest.TestCase):
    def test_PayloadStock(self):
        pl = Payload()
        pl.bld = "test"
        data = pl.to_dict()
        self.assertEqual("test", data['bld'])
        self.assertEqual(None, data.get('typeNo', None))

    def test_PayloadStockBuilder(self):
        pl = (PayloadBuilder("all_stock_prices")
              .set_attribute('mktId', "ALL")
              .set_attribute('trdDd', "20220801")
              .build())
        target = {
            "bld": "dbms/MDC/STAT/standard/MDCSTAT01501",
            "locale": "ko_KR",
            "mktId": "ALL",
            "trdDd": "20220801",
            "share": 1,
            "money": 1,
        }
        data = pl.to_dict()
        for k, v in target.items():
            self.assertEqual(v, data[k])


if __name__ == '__main__':
    unittest.main()

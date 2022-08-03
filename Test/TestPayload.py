import unittest

from KrxApi.payload import PayloadStock
from KrxApi.payload.builder import PayloadStockBuilder
from KrxApi.resources import *


class TestPayload(unittest.TestCase):
    def test_PayloadStock(self):
        pl = PayloadStock()
        pl.bld = "test"
        data = pl.to_dict()
        self.assertEqual("test", data['bld'])
        self.assertEqual(None, data.get('typeNo', None))

    def test_PayloadStockBuilder(self):
        pl = (PayloadStockBuilder()
              .set_bld(BLD.ALL_STOCKS)
              .set_mktId("ALL")
              .set_trdDd("20220801")
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

import unittest

from KrxApi.payload import Payload
from KrxApi.payload.builder import PayloadBuilder
from KrxApi.resources.schemas import schemas, Attr


class TestPayload(unittest.TestCase):
    def test_PayloadStock(self):
        pl = Payload()
        pl.bld = "test"
        data = pl.to_dict()
        self.assertEqual("test", data['bld'])
        self.assertEqual(None, data.get('typeNo', None))

    def test_PayloadBuilder(self):
        pl = (PayloadBuilder("all_stock_prices")
              .set_attribute('mktId', "ALL")
              .set_attribute('trdDd', "20220801")
              .build())
        target = {}
        for k, v in schemas['all_stock_prices'].items():
            target[k] = v.get(Attr.value)
        target.update(
            {
                "trdDd": "20220801",
                "mktId": "ALL",
            }
        )
        data = pl.to_dict()
        for k, v in target.items():
            self.assertEqual(v, data[k])


if __name__ == '__main__':
    unittest.main()

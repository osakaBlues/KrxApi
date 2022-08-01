import unittest

import KrxApi


class TestKrdApi(unittest.TestCase):
    def test_requestStatus(self):
        krx = KrxApi.Krx()
        res = krx.get_all_stocks_price()
        self.assertEqual("1", res)
        res = krx.get_all_stocks_flrate()
        self.assertEqual("1", res)


if __name__ == '__main__':
    unittest.main()

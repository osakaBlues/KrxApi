import unittest

from KrxApi.KrxRequest import *
from KrxApi.resources import *


class KrxRequestTest(unittest.TestCase):

    def test_KrxRequest(self):
        request = KrxRequest(all_stock_prices, {"mktId":"ALL", "trdDd":"20220809"})
        constraints = request.parameter_constraints
        tar_keys = ('mktId', 'trdDd')
        for i in constraints.keys():
            self.assertTrue(i in tar_keys)
        self.assertEqual('choice', constraints['mktId']['type'])
        self.assertEqual('date', constraints['trdDd']['type'])

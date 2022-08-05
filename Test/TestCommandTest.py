import unittest

from KrxApi.payload.builder import PayloadStockBuilder
from KrxApi.command import Command
from KrxApi.resources import *
from KrxApi.KrxResponse import KrxResponse

from mock import ConnectionMock


class CommandTest(unittest.TestCase):

    def test_Command_all_stock(self):
        connection = ConnectionMock((PayloadStockBuilder()
                                       .set_bld(BLD.ALL_STOCKS)
                                       .set_mktId("ALL")
                                       .set_trdDd("20220801")
                                       .build()), URLS.STOCK_INFO_CMD)
        cmd = Command(connection)
        self.assertEqual(KrxResponse, type(cmd.execute()))


if __name__ == '__main__':
    unittest.main()

import unittest

from KrxApi.payload.builder import PayloadBuilder
from KrxApi.command import Command
from KrxApi.resources import *
from KrxApi.KrxResponse import KrxResponse

from mock import ConnectionMock


class CommandTest(unittest.TestCase):

    def test_Command_all_stock(self):

        connection = ConnectionMock((PayloadBuilder(schemas.get_schema(schemas.all_stock_prices))
                                    .set_attribute("mktId", "ALL")
                                    .set_attribute("trdDd", "20220801")
                                    .build()), URLS.STOCK_INFO_CMD)
        cmd = Command(connection)
        self.assertEqual(KrxResponse, type(cmd.execute()))


if __name__ == '__main__':
    unittest.main()

from KrxApi.command import Command
from KrxApi.payload import PayloadStock
from KrxApi.util.get_time import get_formatted_date_today, get_formatted_date_week_before
from KrxApi.resources import *


class Krx:
    def get_all_stocks_price(self,
                             mktId=MARKETS.ALL,
                             trdDd=get_formatted_date_today(),
                             share=SHARE.ONE,
                             money=MONEY.WON):
        pl = PayloadStock()
        pl.bld = BLD.ALL_STOCK
        pl.mktId = mktId
        pl.trdDd = trdDd
        pl.share = share
        pl.money = money
        cmd = Command(pl)
        result = cmd.execute()
        return result

    def get_all_stocks_flrate(self,
                              mktId=MARKETS.ALL,
                              strtDd=get_formatted_date_week_before(),
                              endDd=get_formatted_date_today(),
                              share=SHARE.ONE,
                              money=MONEY.WON):
        pl = PayloadStock()
        pl.mktId = mktId
        pl.share = share
        pl.money = money
        pl.endDd = endDd
        pl.strtDd = strtDd
        cmd = Command(pl)
        result = cmd.execute()
        return result


__all__ = ["Krx"]

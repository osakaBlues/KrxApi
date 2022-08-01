from KrxApi.command import Command
from KrxApi.payload import PayloadAllStocks, PayloadAllStocksFlRate
from KrxApi.util.get_time import get_formatted_date_today, get_formatted_date_week_before


class Krx:
    def get_all_stocks_price(self,
                             mktid="ALL",
                             trddd=get_formatted_date_today(),
                             share="1",
                             money="1"):
        pl = PayloadAllStocks(mktid, trddd, share, money)
        cmd = Command(pl)
        result = cmd.execute()
        return result

    def get_all_stocks_flrate(self,
                              mktid="ALL",
                              strtdd=get_formatted_date_week_before(),
                              enddd=get_formatted_date_today(),
                              share="1",
                              money="1"):
        pl = PayloadAllStocksFlRate(mktid, strtdd, enddd, share, money)
        cmd = Command(pl)
        result = cmd.execute()
        return result


__all__ = ["Krx"]

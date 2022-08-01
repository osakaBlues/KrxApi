from KrxApi.command import Command
from KrxApi.payload import PayloadAllStocks
from KrxApi.util.get_time import get_formatted_date


class Krx:
    def get_all_stocks_price(self,
                             mktid="ALL",
                             trddd=get_formatted_date(),
                             share="1",
                             money="1"):
        pl = PayloadAllStocks(mktid=mktid, trddd=trddd, share=share, money=money)
        cmd = Command(pl)
        result = cmd.execute()
        return result


__all__ = ["Krx"]

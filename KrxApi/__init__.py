from KrxApi.command import Command
from KrxApi.payload import PayloadStock
from KrxApi.util.get_time import get_formatted_date_today, get_formatted_date_week_before
from KrxApi.resources import *
from KrxApi.payload.builder import PayloadStockBuilder
from KrxApi.connection import Connection


class Krx:
    @staticmethod
    def get_all_stock_prices(mktId=MARKETS.ALL,
                             trdDd=get_formatted_date_today()):
        return Command(
                Connection(
                    (PayloadStockBuilder()
                     .set_bld(BLD.ALL_STOCKS)
                     .set_mktId(mktId)
                     .set_trdDd(trdDd)
                     .build()), URLS.STOCK_INFO_CMD)).execute()

    @staticmethod
    def get_all_stock_fluctuation_rates(mktId=MARKETS.ALL,
                                        strtDd=get_formatted_date_week_before(),
                                        endDd=get_formatted_date_today()):
        return Command(
                Connection(
                    (PayloadStockBuilder()
                     .set_bld(BLD.ALL_STOCK_FLUCTUATION_RATES)
                     .set_mktId(mktId)
                     .set_trdDd(strtDd)
                     .set_endDd(endDd)
                     .build()), URLS.STOCK_INFO_CMD)).execute()

    def get_stock_price(self,
                        ticker,
                        strtDd=get_formatted_date_week_before(),
                        endDd=get_formatted_date_today()):
        pl = PayloadStock()
        pl.bld = BLD.A_STOCK_PRICE
        """
        todo
        payload에 데이터 넣기
        """
        pl.bld = BLD.A_STOCK_PRICE
        cmd = Command(pl)
        result = cmd.execute()
        return result

    """
    검색에서는 mktId 대신 mktsel
    consonant 1~15 정수 : ㄱ, ㄴ, ㄷ, ... , ㅎ, a~z 까지 15개
    """

    def search_indv_stock(self,
                          mktsel="ALL",
                          typeNO="0",
                          searchText="",
                          consonant=None):
        pl = PayloadStock()
        """
        todo
        payload에 데이터 넣기
        """
        pl.bld = BLD.A_STOCK_PRICE
        cmd = Command(pl)
        result = cmd.execute()
        return result


__all__ = ["Krx"]

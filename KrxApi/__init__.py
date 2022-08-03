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
    typeNo는 뭔지 알수없음
    """

    @staticmethod
    def search_a_stock(mktsel=MARKETS.ALL,
                       typeNo="0",
                       searchText="",
                       consonant=None):
        return Command(
            Connection(
                (PayloadStockBuilder()
                 .set_bld(BLD.SEARCH_A_STOCK)
                 .set_mktsel(mktsel)
                 .set_typeNo(typeNo)
                 .set_searchText(searchText)
                 .set_consonant(consonant)
                 .build()), URLS.STOCK_INFO_CMD)).execute()


__all__ = ["Krx"]

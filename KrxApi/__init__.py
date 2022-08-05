from KrxApi.command import Command
from KrxApi.util.get_time import get_formatted_date_today, get_formatted_date_week_before
from KrxApi.resources import *
from KrxApi.payload.builder import PayloadBuilder
from KrxApi.connection import Connection


class Krx:
    @staticmethod
    def get_ticker(searchText: str,
                   mktsel=MARKETS.ALL):
        res = Command(
            Connection(
                (PayloadBuilder("search_a_stock")
                 .set_attribute('mktsel', mktsel)
                 .set_attribute('searchText', searchText)
                 .build()), URLS.STOCK_INFO_CMD)).execute()
        return res.get_ticker()

    @staticmethod
    def get_all_stock_prices(mktId=MARKETS.ALL,
                             trdDd=get_formatted_date_today()):
        return Command(
            Connection(
                (PayloadBuilder("all_stock_prices")
                 .set_attribute('mktId', mktId)
                 .set_attribute('trdDd', trdDd)
                 .build()), URLS.STOCK_INFO_CMD)).execute()

    @staticmethod
    def get_all_stock_fluctuation_rates(mktId=MARKETS.ALL,
                                        strtDd=get_formatted_date_week_before(),
                                        endDd=get_formatted_date_today()):
        return Command(
            Connection(
                (PayloadBuilder("all_stock_fluctuations")
                 .set_attribute('mktId', mktId)
                 .set_attribute('strtDd', strtDd)
                 .set_attribute('endDd', endDd)
                 .build()), URLS.STOCK_INFO_CMD)).execute()

    @staticmethod
    def get_stock_price_info(isuCd,
                             strtDd=get_formatted_date_week_before(),
                             endDd=get_formatted_date_today()):
        return Command(
            Connection(
                (PayloadBuilder('stock_price_info')
                 .set_attribute('isuCd', isuCd)
                 .set_attribute('strtDd', strtDd)
                 .set_attribute('endDd', endDd)
                 .build()), URLS.STOCK_INFO_CMD)).execute()


__all__ = ["Krx"]

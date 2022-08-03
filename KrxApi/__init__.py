from KrxApi.command import Command
from KrxApi.util.get_time import get_formatted_date_today, get_formatted_date_week_before
from KrxApi.resources import *
from KrxApi.payload.builder import PayloadBuilder
from KrxApi.connection import Connection


class Krx:
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

    """
    todo 
    인자 autocomplete 할 방법 찾아 보기
    """
    @staticmethod
    def get_stock_price_info(tboxisuCd_finder_stkisu0_3="005930/삼성전자",
                             isuCd="KR7005930003",
                             isuCd2="KR7005930003",
                             codeNmisuCd_finder_stkisu0_0="삼성전자",
                             param1isuCd_finder_stkisu0_0="ALL",
                             strtDd=get_formatted_date_week_before(),
                             endDd=get_formatted_date_today()):
        return Command(
            Connection(
                (PayloadStockBuilder()
                 .set_bld(BLD.A_STOCK_PRICE_INFO)
                 .set_tboxisuCd_finder_stkisu0_3(tboxisuCd_finder_stkisu0_3)
                 .set_isuCd(isuCd)
                 .set_isuCd2(isuCd2)
                 .set_codeNmisuCd_finder_stkisu0_0(codeNmisuCd_finder_stkisu0_0)
                 .set_param1isuCd_finder_stkisu0_0(param1isuCd_finder_stkisu0_0)
                 .set_strtDd(strtDd)
                 .set_endDd(endDd)
                 .build()), URLS.STOCK_INFO_CMD)).execute()

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

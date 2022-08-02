from KrxApi.command import BldCommand
from KrxApi.payload import PayloadStock
from KrxApi.util.get_time import get_formatted_date_today, get_formatted_date_week_before
from KrxApi.resources import *
from KrxApi.payload.builder import PayloadStockBuilder


class Krx:
    def get_all_stock_prices(self,
                             mktId=MARKETS.ALL,
                             trdDd=get_formatted_date_today()):
        return BldCommand(
            PayloadStockBuilder()
            .set_bld(BLD.ALL_STOCKS)
            .set_mktId(mktId)
            .set_trdDd(trdDd)
            .build()
        ).execute()

    def get_all_stock_fluctuation_rates(self,
                                        mktId=MARKETS.ALL,
                                        strtDd=get_formatted_date_week_before(),
                                        endDd=get_formatted_date_today()):
        return BldCommand(
            PayloadStockBuilder()
            .set_bld(BLD.ALL_STOCK_FLUCTUATION_RATES)
            .set_mktId(mktId)
            .set_trdDd(strtDd)
            .set_endDd(endDd)
            .build()
        ).execute()

    def get_stock_price(self,
                        tboxisuCd_finder_stkisu0_3="005930/삼성전자",
                        isuCd="KR7005930003",
                        isuCd2="KR7005930003",
                        codeNmisuCd_finder_stkisu0_3="삼성전자",
                        param1isuCd_finder_stkisu0_3="ALL",
                        strtDd=get_formatted_date_week_before(),
                        endDd=get_formatted_date_today(),
                        share=SHARE.ONE,
                        money=MONEY.WON):
        pl = PayloadStock()
        pl.bld = BLD.A_STOCK_PRICE
        """
        todo
        payload에 데이터 넣기
        """
        pl.bld = BLD.A_STOCK_PRICE
        cmd = BldCommand(pl)
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
        cmd = BldCommand(pl)
        result = cmd.execute()
        return result


__all__ = ["Krx"]

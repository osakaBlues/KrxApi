from KrxApi.command import BldCommand
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
        cmd = BldCommand(pl)
        result = cmd.execute()
        return result

    def get_all_stocks_flrate(self,
                              mktId=MARKETS.ALL,
                              strtDd=get_formatted_date_week_before(),
                              endDd=get_formatted_date_today(),
                              share=SHARE.ONE,
                              money=MONEY.WON):
        pl = PayloadStock()
        pl.bld = BLD.ALL_STOCK_FLRATE
        pl.mktId = mktId
        pl.share = share
        pl.money = money
        pl.endDd = endDd
        pl.strtDd = strtDd
        cmd = BldCommand(pl)
        result = cmd.execute()
        return result

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
        pl.bld = BLD.INDV_STOCK_PRICE
        """
        todo
        payload에 데이터 넣기
        """
        pl.bld = BLD.INDV_STOCK_PRICE
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
        pl.bld = BLD.INDV_STOCK_PRICE
        cmd = BldCommand(pl)
        result = cmd.execute()
        return result


__all__ = ["Krx"]

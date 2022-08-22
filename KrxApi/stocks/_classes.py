from ..util.get_time import *
from ..KrxRequest import *
from ..resources import *


class StockService:
    def __init__(self, request: KrxRequest, data_process):
        self._request: KrxRequest = request
        self._data_process = data_process
        self._data = None

    def load(self):
        self._data = self._request.run()
        self._data_process.set_data(self._data)
        return self

    def get_data(self, **kargs):
        if self._data is None:
            raise ValueError("Stock data is not loaded yet.")
        return self._data_process.set_params(**kargs).filter().to_dataframe().get_data()


class SearchStock(StockService):
    def __init__(self,
                 searchText: str = "삼성전자",
                 mktsel=MARKETS.ALL):
        from ..DataProcessing import ProcessSearchAStock
        super().__init__(
            StockInfoRequest(search_stock, searchText=searchText, mktsel=mktsel),
            ProcessSearchAStock())

    def get_data(self):
        return super().get_data()

    def get_full_code(self):
        if self._data is None:
            raise ValueError("Stock data is not loaded yet.")
        return self._data_process.get_full_code()


class AllStockPrice(StockService):
    def __init__(self,
                 mktId=MARKETS.ALL,
                 trdDd=get_formatted_date_today()):
        from ..DataProcessing import ProcessAllStockPrice
        super().__init__(
            StockInfoRequest(all_stock_prices, mktId=mktId, trdDd=trdDd),
            ProcessAllStockPrice())

    def get_data(self,
                 full_code=False,
                 fluc_rate=False,
                 trade_amount=False,
                 trade_money=False,
                 market_capitalization=False,
                 total_stocks=False):
        return super().get_data(
            full_code=full_code,
            fluc_rate=fluc_rate,
            trade_amount=trade_amount,
            trade_money=trade_money,
            market_capitalization=market_capitalization,
            total_stocks=total_stocks
        )


class AllStockFluctuationRate(StockService):

    def __init__(self,
                 mktId=MARKETS.ALL,
                 strtDd=get_formatted_date_week_before(),
                 endDd=get_formatted_date_today()):
        from ..DataProcessing import ProcessAllStockFluctuationRate
        super().__init__(
            StockInfoRequest(all_stock_fluctuations, mktId=mktId, strtDd=strtDd, endDd=endDd),
            ProcessAllStockFluctuationRate())

    def get_data(self,
                 full_code=False,
                 fluc_rate=True,
                 trade_amount=False,
                 trade_money=False):
        return super().get_data(
            full_code=full_code,
            fluc_rate=fluc_rate,
            trade_amount=trade_amount,
            trade_money=trade_money
        )


class StockPriceInfo(StockService):
    def __init__(self,
                 isuCd="KR7005930003",
                 strtDd=get_formatted_date_week_before(),
                 endDd=get_formatted_date_today()):
        from ..DataProcessing import ProcessAStockPriceInfo
        super().__init__(
            StockInfoRequest(stock_price_info, isuCd=isuCd, strtDd=strtDd, endDd=endDd),
            ProcessAStockPriceInfo())

    def get_data(self,
                 fluc_rate=False,
                 trade_amount=False,
                 trade_money=False,
                 market_capitalization=False,
                 total_stocks=False):
        return super().get_data(
            fluc_rate=fluc_rate,
            trade_amount=trade_amount,
            trade_money=trade_money,
            market_capitalization=market_capitalization,
            total_stocks=total_stocks
        )

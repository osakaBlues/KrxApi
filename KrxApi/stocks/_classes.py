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

    def get_data(self):
        if self._data is None:
            raise ValueError("Stock data is not loaded yet.")


class SearchStock(StockService):
    def __init__(self,
                 searchText: str = "삼성전자",
                 mktsel=MARKETS.ALL):
        from ..DataProcessing import ProcessSearchAStock
        super().__init__(
            StockInfoRequest(search_stock, searchText=searchText, mktsel=mktsel),
            ProcessSearchAStock())

    def get_data(self):
        super().get_data()
        return self._data_process.set_params().filter()

    def get_full_code(self):
        super().get_data()
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
        super().get_data()

        return self._data_process.set_params(full_code,
                                             fluc_rate,
                                             trade_amount,
                                             trade_money,
                                             market_capitalization,
                                             total_stocks).filter()


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
        super().get_data()

        return self._data_process.set_params(full_code,
                                             fluc_rate,
                                             trade_amount,
                                             trade_money).filter()


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
        super().get_data()

        return self._data_process.set_params(fluc_rate,
                                             trade_amount,
                                             trade_money,
                                             market_capitalization,
                                             total_stocks).filter()

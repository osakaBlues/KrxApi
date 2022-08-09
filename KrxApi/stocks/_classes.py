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

    def get_data(self):
        if self._data is None:
            raise ValueError("Stock data is not loaded yet.")


class SearchStock(StockService):
    def __init__(self, searchText: str, mktsel=MARKETS.ALL):
        super().__init__(
            StockInfoRequest(search_stock, searchText=searchText, mktsel=mktsel),
            None)


class AllStockPrice(StockService):
    def __init__(self, mktId=MARKETS.ALL, trdDd=get_formatted_date_today()):
        super().__init__(
            StockInfoRequest(all_stock_prices, mktId=mktId, trdDd=trdDd),
            None)

    def get_data(self,
             full_code=False,
             fluc_rate=False,
             trade_amount=False,
             trade_money=False,
             market_capitalization=False,
             total_stocks=False):
        super().get_data()
        from ..DataProcessing import ProcessAllStockPrice
        _process_data = ProcessAllStockPrice(self._data)
        return _process_data.set_params(full_code,
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

        super().__init__(
            StockInfoRequest(all_stock_fluctuations, mktId=mktId, strtDd=strtDd, endDd=endDd),
            None)

    def get_data(self,
             full_code=False,
             fluc_rate=True,
             trade_amount=False,
             trade_money=False):
        super().get_data()

        from ..DataProcessing import ProcessAllStockFluctuationRate

        _process_data = ProcessAllStockFluctuationRate(self._data)

        return _process_data.set_params(full_code,
                                        fluc_rate,
                                        trade_amount,
                                        trade_money).filter()


class StockPriceInfo(StockService):
    def __init__(self, isuCd,
                 strtDd=get_formatted_date_week_before(),
                 endDd=get_formatted_date_today()):
        super().__init__(
            StockInfoRequest(stock_price_info, isuCd=isuCd, strtDd=strtDd, endDd=endDd),
            None)

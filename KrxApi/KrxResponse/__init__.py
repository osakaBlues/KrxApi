from .Ticker import Ticker


class KrxResponse:
    def __init__(self, data: any):
        self.data: any = data

    def set_data(self, data: any):
        self.data = data
        
    def get_data(self) -> any:
        return self.data

    def get_ticker(self) -> Ticker:
        try:
            result = self.data.get('block1')[0]
        except KeyError:
            raise Exception('This object is not Ticker')

        return Ticker(result.get('codeName'),
                      result.get('full_code'),
                      result.get('marketCode'),
                      result.get('short_code'))

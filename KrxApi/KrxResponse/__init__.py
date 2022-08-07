from .Ticker import Ticker


class KrxResponse:
    def __init__(self):
        self.data: any = None

    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data

    def get_ticker(self):
        try:
            result = self.data.get('block1')[0]
        except KeyError:
            raise Exception('티커가 아닙니다.')

        return Ticker(result.get('codeName'),
                      result.get('full_code'),
                      result.get('marketCode'),
                      result.get('short_code'))

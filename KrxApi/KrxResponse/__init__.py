from .Ticker import Ticker


class KrxResponse:
    def __init__(self, data: any):
        self.data: any = data

    def set_data(self, data: any):
        self.data = data
        
    def get_data(self) -> any:
        return self.data

    def to_dataframe(self):
        import pandas as pd
        self.data = pd.DataFrame([i for i in self.get_data() if type(i) == dict])
        return self

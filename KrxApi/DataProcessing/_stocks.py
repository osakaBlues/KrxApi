class Process:
    def __init__(self):
        self._params = None
        self._data = None
        self._data_index = None

    def set_data(self, data):
        self._data = data

    def filter(self):
        import pandas as pd

        result = {}
        names = {}

        from ._names import names_total as nt

        for n in self._params.keys():
            names[n] = nt.get(n)

        for k in self._params.keys():
            if self._params.get(k) is True:
                result[names.get(k)] = []

        for stk in self._data[self._data_index]:
            for k in self._params.keys():
                if self._params.get(k) is True:
                    result[names.get(k)].append(stk.get(k))

        result["현재 시각"] = self._data.get("CURRENT_DATETIME")
        return pd.DataFrame(result)


class ProcessAllStockPrice(Process):
    def set_params(self,
                   full_code,
                   fluc_rate,
                   trade_amount,
                   trade_money,
                   market_capitalization,
                   total_stocks):
        self._data_index = "OutBlock_1"
        self._params = {"ISU_SRT_CD": True,
                        "ISU_CD": full_code,
                        "ISU_ABBRV": True,
                        "MKT_NM": True,
                        "SECT_TP_NM": False,
                        "TDD_CLSPRC": True,
                        "FLUC_TP_CD": False,
                        "CMPPREVDD_PRC": True,
                        "FLUC_RT": fluc_rate,
                        "TDD_OPNPRC": False,
                        "TDD_HGPRC": False,
                        "TDD_LWPRC": False,
                        "ACC_TRDVOL": trade_amount,
                        "ACC_TRDVAL": trade_money,
                        "MKTCAP": market_capitalization,
                        "LIST_SHRS": total_stocks,
                        "MKT_ID": False}
        return self


class ProcessAllStockFluctuationRate(Process):
    def set_params(self,
                   full_code,
                   fluc_rate,
                   trade_amount,
                   trade_money):
        self._data_index = "OutBlock_1"
        self._params = {"ISU_SRT_CD": full_code,
                        "ISU_ABBRV": True,
                        "BAS_PRC": True,
                        "TDD_CLSPRC": True,
                        "CMPPREVDD_PRC": True,
                        "FLUC_RT": fluc_rate,
                        "ACC_TRDVOL": trade_amount,
                        "ACC_TRDVAL": trade_money,
                        "FLUC_TP": False}
        return self


class ProcessAStockPriceInfo(Process):
    def set_params(self,
                   fluc_rate,
                   trade_amount,
                   trade_money,
                   market_capitalization,
                   total_stocks):
        self._data_index = "output"
        self._params = {"ACC_TRDVAL": trade_money,
                        "ACC_TRDVOL": trade_amount,
                        "CMPPREVDD_PRC": True,
                        "FLUC_RT": fluc_rate,
                        "FLUC_TP_CD": False,
                        "LIST_SHRS": total_stocks,
                        "MKTCAP": market_capitalization,
                        "TDD_CLSPRC": True,
                        "TDD_HGPRC": False,
                        "TDD_LWPRC": False,
                        "TDD_OPNPRC": False,
                        "TRD_DD": True}
        return self


class ProcessSearchAStock(Process):
    def set_params(self):
        self._data_index = "block1"
        self._params = {'full_code': True,
                        'short_code': True,
                        'codeName': True,
                        'marketCode': True,
                        'marketName': True,
                        'marketEngName': True,
                        'ord1': False,
                        'ord2': False}
        return self

    def get_full_code(self):
        self._data_index = "block1"
        return self._data[self._data_index][0].get('full_code')

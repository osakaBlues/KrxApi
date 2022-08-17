class Process:
    def __init__(self, data):
        self._params = None
        self._data = data

    def filter(self):
        result = []
        names = {}

        from ._names import names_total as nt

        for n in self._params.keys():
            names[n] = nt.get(n)

        for stk in self._data["OutBlock_1"]:
            temp = {}
            for k in self._params.keys():
                if self._params.get(k) is True:
                    temp[names.get(k)] = stk.get(k)
            result.append(temp)

        result.append(self._data["CURRENT_DATETIME"])
        return result


class ProcessAllStockPrice(Process):
    def set_params(self,
                   full_code,
                   fluc_rate,
                   trade_amount,
                   trade_money,
                   market_capitalization,
                   total_stocks):
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
    def set_params(self):
        self._params = {}
        return self


class ProcessSearchAStock(Process):
    def set_params(self):
        self._params = {}
        return self

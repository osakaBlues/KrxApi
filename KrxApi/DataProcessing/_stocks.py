class ProcessAllStockPrice:
    def __init__(self, data):
        self._data = data

    def filter(self,
               full_code,
               fluc_rate,
               trade_amount,
               trade_money,
               market_capitalization,
               total_stocks):

        from ._names import names_total as nt

        params = {"ISU_SRT_CD": True,
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

        result = []
        names = {}
        for n in params.keys():
            names[n] = nt.get(n)

        for stk in self._data["OutBlock_1"]:
            temp = {}
            for k in params.keys():
                if params.get(k) is True:
                    temp[names.get(k)] = stk.get(k)
            result.append(temp)

        result.append(self._data["CURRENT_DATETIME"])
        return result

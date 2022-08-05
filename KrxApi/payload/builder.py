from KrxApi.payload import Payload, PayloadStock


class PayloadBuilder:
    __slots__ = ['_payload']

    def build(self) -> Payload:
        return self._payload


class PayloadStockBuilder(PayloadBuilder):
    def __init__(self):
        self._payload: PayloadStock = PayloadStock()

    def set_bld(self, bld: str) -> 'PayloadStockBuilder':
        self._payload.bld = bld
        return self

    def set_mktId(self, mktId: str) -> 'PayloadStockBuilder':
        self._payload.mktId = mktId
        return self

    def set_trdDd(self, trdDd: str) -> 'PayloadStockBuilder':
        self._payload.trdDd = trdDd
        return self

    def set_strtDd(self, strtDd: str) -> 'PayloadStockBuilder':
        self._payload.strtDd = strtDd
        return self

    def set_endDd(self, endDd: str) -> 'PayloadStockBuilder':
        self._payload.endDd = endDd
        return self

    def set_mktsel(self, mktsel: str) -> 'PayloadStockBuilder':
        self._payload.mktsel = mktsel
        return self

    def set_typeNo(self, typeNo: str) -> 'PayloadStockBuilder':
        self._payload.typeNo = typeNo
        return self

    def set_searchText(self, searchText: str) -> 'PayloadStockBuilder':
        self._payload.searchText = searchText
        return self

    def set_consonant(self, consonant: str) -> 'PayloadStockBuilder':
        self._payload.consonant = consonant
        return self

    def set_tboxisuCd_finder_stkisu0_3(self, tboxisuCd_finder_stkisu0_3: str) -> 'PayloadStockBuilder':
        self._payload.tboxisuCd_finder_stkisu0_3 = tboxisuCd_finder_stkisu0_3
        return self

    def set_isuCd(self, isuCd: str) -> 'PayloadStockBuilder':
        self._payload.isuCd = isuCd
        return self

    def set_isuCd2(self, isuCd2: str) -> 'PayloadStockBuilder':
        self._payload.isuCd2 = isuCd2
        return self

    def set_codeNmisuCd_finder_stkisu0_0(self, codeNmisuCd_finder_stkisu0_0: str) -> 'PayloadStockBuilder':
        self._payload.codeNmisuCd_finder_stkisu0_0 = codeNmisuCd_finder_stkisu0_0
        return self

    def set_param1isuCd_finder_stkisu0_0(self, param1isuCd_finder_stkisu0_0: str) -> 'PayloadStockBuilder':
        self._payload.param1isuCd_finder_stkisu0_0 = param1isuCd_finder_stkisu0_0
        return self

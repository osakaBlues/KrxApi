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
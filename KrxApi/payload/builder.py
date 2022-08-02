from KrxApi.payload import Payload, PayloadStock
from typing import Self


class PayloadBuilder:
    _payload: Payload

    def __init__(self):
        self._payload = Payload()

    def build(self) -> Payload:
        return self._payload


class PayloadStockBuilder(PayloadBuilder):
    _payload: PayloadStock

    def set_bld(self, bld: str) -> Self:
        self._payload.bld = bld
        return self

    def set_mktId(self, mktId: str) -> Self:
        self._payload.mktId = mktId
        return self

    def set_trdDd(self, trdDd: str) -> Self:
        self._payload.trdDd = trdDd
        return self

    def set_strtDd(self, strtDd: str) -> Self:
        self._payload.strtDd = strtDd
        return self

    def set_endDd(self, endDd: str) -> Self:
        self._payload.endDd = endDd
        return self
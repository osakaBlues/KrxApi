"""
    요청을 위한 모듈
    요청에 필요한 객체들을 모아 실행시킨다.
"""
from datetime import datetime

from KrxApi.command import Command
from KrxApi.connection import Connection
from KrxApi.payload.builder import PayloadBuilder
from KrxApi.resources.schemas import *
from KrxApi.resources.SchemaError import SchemaError
from KrxApi.resources import URLS

from typing import Optional


class KrxRequest:
    """
        Args:
            request_id (str): schema 중 사용할 id
            args (dict): 요청에 넣을 파라미터 (payload에 들어갈)
    """
    def __init__(self, request_id: str, args: dict):
        self._id: str = request_id
        self.parameter_constraints: dict = {}
        self._command: Optional[Command] = None
        for attr, value in schemas[self._id].items():
            if type(value) is not dict:
                raise SchemaError(attr)
            if value.get(Attr.required):
                self.parameter_constraints[attr] = value.get(Attr.type)
        for k, v in args.items():
            self.is_valid_param(k, v)
        self._payload = (PayloadBuilder(self._id)
                         .set_attributes(args)
                         .build())

    def is_valid_param(self, key: str, value: str) -> bool:
        constraint = self.parameter_constraints.get(key)
        if constraint is None:
            return False
        cons_type = constraint.get(Attr.type)
        cons_value = constraint.get(Attr.value)
        if Type.choice == cons_type:
            return value in cons_value
        elif Type.date == cons_type:
            try:
                datetime.strptime(value, cons_value)
            except ValueError:
                return False
        else:
            return False

    def run(self) -> any:
        if self._command is None:
            raise NotImplementedError
        return self._command.execute().get_data()


class AllStockPriceRequest(KrxRequest):
    def __init__(self, **kwargs):
        super().__init__(all_stock_prices, args=kwargs)
        self._command = Command(Connection(self._payload, URLS.STOCK_INFO_CMD))


class AllStockFluctuationRateRequest(KrxRequest):
    def __init__(self, **kwargs):
        super().__init__(all_stock_fluctuations, args=kwargs)
        self._command = Command(Connection(self._payload, URLS.STOCK_INFO_CMD))

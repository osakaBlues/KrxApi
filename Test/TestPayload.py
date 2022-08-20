import unittest

from KrxApi.payload import Payload
from KrxApi.payload.builder import PayloadBuilder
from KrxApi.resources.schemas import schemas, Attr
from KrxApi.resources.SchemaError import *


class TestPayload(unittest.TestCase):

    def setUp(self) -> None:
        self.immutable_fixture = {
            "immutable": {
                Attr.value: "test",
                Attr.mutable: False
            },
        }
        self.required_fixture = {
            "required": {
                Attr.required: True
            }
        }

    def test_PayloadStock(self):
        pl = Payload()
        pl_empty = Payload()
        pl.bld = "test"
        data = pl.to_dict()
        self.assertEqual("test", data['bld'])
        self.assertEqual(None, data.get('typeNo', None))
        self.assertEqual(dict(), pl_empty.to_dict())

    def test_PayloadBuilder(self):
        builder1 = PayloadBuilder(self.immutable_fixture)
        builder2 = PayloadBuilder(self.required_fixture)
        with self.assertRaises(SchemaError):
            builder1.set_attribute("immutable", "abc")
        with self.assertRaises(SchemaError):
            builder1.set_attribute("wrong key", "abc")
        with self.assertRaises(SchemaError):
            builder2.build()

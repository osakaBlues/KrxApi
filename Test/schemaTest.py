import unittest
from KrxApi.resources.schemas import *


class SchemaTest(unittest.TestCase):
    def test_validate_schema_value(self):
        none_value = None
        schema_value1 = {
            Attr.value: "str",
            Attr.mutable: True,
            Attr.type: {},
            Attr.required: True
        }
        schema_value_number = {
            Attr.value: 1
        }
        schema_value3 = {
            Attr.type: False
        }
        self.assertEqual(False, validate_schema_value(none_value))
        self.assertEqual(True, validate_schema_value(schema_value_number))
        self.assertEqual(True, validate_schema_value(schema_value1))
        self.assertEqual(False, validate_schema_value(schema_value3))

    def test_validate_schema(self):
        for v in schemas.values():
            self.assertEqual(True, validate_schema(v))

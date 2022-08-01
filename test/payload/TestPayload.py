import unittest

from payload import PayloadStock


class TestPayload(unittest.TestCase):
    def test_PayloadStock(self):
        pl = PayloadStock()
        pl.bld = "test"
        data = pl.to_dict()
        self.assertEqual("test", data['bld'])


if __name__ == '__main__':
    unittest.main()

from KrxApi.connection import Connection
import json

_input_file1 = 'fixtures/real_data_input_all_stock.json'
_output_file1 = 'fixtures/real_data_output_all_stock.txt'


class ConnectionMock(Connection):
    _tar_payload: dict
    _src_payload: dict

    def _cmp_dict(self, keys):
        for key in keys:
            if self._tar_payload[key] != self._src_payload[key]:
                return False
        return True

    def get_data(self) -> str:
        self._src_payload = self.payload.to_dict()
        with open(_input_file1, 'r') as f:
            dummy = json.loads(f.read())
        self._tar_payload = dummy['payload']
        if self.url == dummy['url']:
            if self._cmp_dict(['bld', 'locale', 'mktId', 'trdDd']):
                with open(_output_file1) as f:
                    result = f.read()
                return result
        raise RuntimeError
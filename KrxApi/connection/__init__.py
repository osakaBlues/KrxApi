import requests
from KrxApi.payload import Payload


class Connection:
    def __init__(self, payload: Payload, url: str = None):
        self.payload: Payload = payload
        self.url: str = url

    def get_data(self) -> str:
        if self.url is None:
            raise ConnectionAbortedError("url이 설정되지 않았습니다.")
        try:
            result = requests.get(self.url, params=self.payload.to_dict())
            if result.status_code != 200:
                raise RuntimeError
        except:
            raise ConnectionError("연결에 실패했습니다.")
        return result.text

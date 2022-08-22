"""
    연결에 관한 모듈
"""
import requests
from KrxApi.payload import Payload


class Connection:
    """
        Args:
            payload (payload): url을 통해 전달할 데이터 객체
            url (str): 요청을 보낼 url
    """
    def __init__(self, payload: Payload, url: str = None):
        self.payload: Payload = payload
        self.url: str = url

    def get_data(self) -> str:
        """
            설정된 정보에 해당하는 연결을 한 후 데이터를 돌려줌
            Returns:
                str: url을 통해 연결을 통해 얻은 데이터
            Raises:
                ConnectionError: 설정한 연결에 실패함, (payload 혹은 url이 잘못 되었거나, 인터넷 연결 문제)
        """
        if self.url is None:
            raise ConnectionAbortedError("The url is not set")
        try:
            result = requests.get(self.url, params=self.payload.to_dict())
            if result.status_code != 200:
                raise RuntimeError
        except requests.exceptions.RequestException as err:
            raise ConnectionError("Failed get data from internet", err)
        return result.text

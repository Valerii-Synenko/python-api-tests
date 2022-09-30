import os

import requests
from requests import post, delete


class BaseApiService(object):
    def __init__(self):
        self.__base_url: str = os.environ["BASE_URL"]
        self.__headers: dict = {"content-type": "application/json"}

    def _post(self, endpoint: str, request_body) -> post:
        return requests.post(
            url=f"{self.__base_url}{endpoint}",
            json=dict(request_body),
            headers=self.__headers,
        )

    def _delete(self, endpoint: str) -> delete:
        return requests.delete(
            url=f"{self.__base_url}{endpoint}", headers=self.__headers
        )

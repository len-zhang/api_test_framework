# -*- coding:utf-8 -*-
import requests
import json


class BaseApi:
    def send_api(self, data: dict):
        # print(json.dumps(data, indent=4))
        r = requests.request(**data).json()
        return r

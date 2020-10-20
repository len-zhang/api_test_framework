# -*- coding:utf-8 -*-
from api.base_api import BaseApi


class WeworkUtils(BaseApi):
    def get_token(self, secret_id):
        corpid = "ww90db737a195a0094"
        corpsecret = secret_id
        token_dict = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        token = self.send_api(token_dict)["access_token"]
        return token

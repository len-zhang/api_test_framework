# -*- coding:utf-8 -*-
from api.base_api import BaseApi
from utils.utils import WeworkUtils


class AddressApi(BaseApi):
    def __init__(self):
        _secret_id = "6iKphtr1w_zn2v_8jobg-XsMDAGXtSOtfP_UOD-gLWY"
        self.token = WeworkUtils().get_token(_secret_id)

    def add_member(self):
        addmember_data = {"method": "post",
                          "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          "params": {"access_token": self.token},
                          "json": {"userid": "gongtengxinyi", "name": "工藤新一",
                                   "mobile": "13800001111", "department": [1]}
                          }
        return self.send_api(addmember_data)

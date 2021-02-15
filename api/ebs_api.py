# -*- coding:utf-8 -*-
from api.base_api import BaseApi
from utils.utils import WeworkUtils, MakeSignature, SetEnv


class EbsApi(BaseApi):
    def __init__(self):
        _env_config = SetEnv.get_url()
        self.url = _env_config["www.unicloud.com"][_env_config["default"]]
        self.aks = _env_config["aks"]
        self.param_config = SetEnv.get_param()
        # _secret_id = "6iKphtr1w_zn2v_8jobg-XsMDAGXtSOtfP_UOD-gLWY"
        # self.token = WeworkUtils().get_token(_secret_id)

    # def add_member(self):
    #     addmember_data = {"method": "post",
    #                       "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create",
    #                       "params": {"access_token": self.token},
    #                       "json": {"userid": "gongtengxinyi", "name": "工藤新一",
    #                                "mobile": "13800001111", "department": [1]}
    #                       }
    #     return self.send_api(addmember_data)

    def describe_ebs(self, param):
        method = "GET"
        describe_ebs_param = MakeSignature().get_url(method, param, self.aks)
        describe_ebs_data = {"method": "get",
                             "url": f"{self.url}/ebs",
                             "params": describe_ebs_param
                             }
        return self.send_api(describe_ebs_data)

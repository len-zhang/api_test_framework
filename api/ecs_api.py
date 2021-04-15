# -*- coding:utf-8 -*-
import logging
from api.base_api import BaseApi
from utils.utils import MakeSignature, SetEnv


class EcsApi(BaseApi):
    def __init__(self):
        _env_config = SetEnv.get_url()
        self.url = _env_config["www.unicloud.com"][_env_config["default"]]
        self.aks = _env_config["aks"]
        self.param_config = SetEnv.get_param()
        self.json_config = SetEnv.get_json()

    def update_ecs_name(self, param):
        method = "GET"
        update_ecs_name_param = MakeSignature().get_url(method, param, self.aks)
        update_ecs_name_data = {"method": "get",
                                "url": f"{self.url}/compute/ecs/instances",
                                "params": update_ecs_name_param
                                }
        logging.info(f"传给send_api作为参数的data数据为{update_ecs_name_data}")
        return self.send_api(update_ecs_name_data)

    def describe_ecs(self, param):
        method = "GET"
        describe_ecs_param = MakeSignature().get_url(method, param, self.aks)
        describe_ecs_data = {"method": "get",
                             "url": f"{self.url}/compute/ecs/instances",
                             "params": describe_ecs_param
                             }
        return self.send_api(describe_ecs_data)

    def run_ecs(self, param, json):
        method = "POST"
        run_ecs_param = MakeSignature().get_url(method, param, self.aks)
        run_ecs_data = {"method": "post",
                        "url": f"{self.url}/compute/ecs/instances",
                        "params": run_ecs_param,
                        "json": json
                        }
        r = self.send_api(run_ecs_data)
        self.json_data = r.json()
        logging.info(f"当前给对象的json_data赋值为{self.json_data}")
        return r

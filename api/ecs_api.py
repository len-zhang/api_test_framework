# -*- coding:utf-8 -*-
from utils.logger import logger
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
        logger.logger.info(f"传给send_api作为参数的data数据为{update_ecs_name_data}")
        r = self.send_api(update_ecs_name_data)
        self.json_data = r.json()
        return r

    def describe_ecs(self, param):
        method = "GET"
        describe_ecs_param = MakeSignature().get_url(method, param, self.aks)
        describe_ecs_data = {"method": "get",
                             "url": f"{self.url}/compute/ecs/instances",
                             "params": describe_ecs_param
                             }
        r = self.send_api(describe_ecs_data)
        self.json_data = r.json()
        return r

    def run_ecs(self, param, json):
        method = "POST"
        run_ecs_param = MakeSignature().get_url(method, param, self.aks)
        run_ecs_data = {"method": "post",
                        "url": f"{self.url}/compute/ecs/instances",
                        "params": run_ecs_param,
                        "json": json
                        }
        r = self.send_api(run_ecs_data)
        self.json_data = r.json()  # 将接口返回结果赋值给self.json_data，替换base_api中的None
        return r

    def delete_ecs(self, param):
        method = "GET"
        delete_ecs_param = MakeSignature().get_url(method, param, self.aks)
        delete_ecs_data = {"method": "get",
                           "url": f"{self.url}/compute/ecs/instances",
                           "params": delete_ecs_param
                           }
        return self.send_api(delete_ecs_data)

    def stop_ecs(self, param):
        method = "GET"
        stop_ecs_param = MakeSignature().get_url(method, param, self.aks)
        stop_ecs_data = {"method": "get",
                         "url": f"{self.url}/compute/ecs/instances",
                         "params": stop_ecs_param
                         }
        r = self.send_api(stop_ecs_data)
        self.json_data = r.json()
        return r

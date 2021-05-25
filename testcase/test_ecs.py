# -*- coding:utf-8 -*-
import logging
import pytest
from api.ecs_api import EcsApi


class TestEcs:
    def setup_class(self):
        self.ecs_api = EcsApi()
        logging.info("=========执行setup_class==========")

    @pytest.mark.parametrize("param", [EcsApi().param_config["ecs_param"]["describe_ecs"]])
    def test_describe_ecs(self, param):
        resp_message = self.ecs_api.describe_ecs(param)
        try:
            assert resp_message.status_code == 200
        except Exception as e:
            raise e

    @pytest.mark.parametrize("param", EcsApi().param_config["ecs_param"]["update_ecs_name"])
    def test_update_ecs_name(self, resource_ready_destroy, param):
        logging.info(f"原始yaml文件中的param为：{param}")
        if "InstanceId" in param.keys():
            param["InstanceId"] = resource_ready_destroy
        else:
            logging.error(f"param配置文件中没有找到InstanceId参数")
        logging.info(f"替换后的yaml文件中param为：{param}")
        resp_message = self.ecs_api.update_ecs_name(param)
        try:
            assert resp_message.status_code == 200
        except Exception as e:
            raise e

    @pytest.mark.parametrize("param", [EcsApi().param_config["ecs_param"]["run_ecs"]])
    @pytest.mark.parametrize("json", [EcsApi().json_config["run_ecs"]])  # 多个参数化装饰器将用笛卡尔积方式组合数据
    def test_run_ecs(self, param, json):
        resp_message = self.ecs_api.run_ecs(param, json)
        result = self.ecs_api.get_jsonpath(expr="$.instanceIds[0]")
        logging.warning(f"对返回json做jsonpath语法筛选后得到的值为{result}")
        try:
            assert resp_message.status_code == 200
            assert "ecs" in result[0]
        except Exception as e:
            raise e

    def test_delete_ecs(self):
        resp_message = self.ecs_api.delete_ecs(EcsApi().param_config["ecs_param"]["delete_ecs"])
        logging.warning(f"接口返回结果为{resp_message.json()}")
        try:
            assert resp_message.status_code == 200
            assert "RequestId" in resp_message.json()
        except Exception as e:
            raise e

    def test_stop_ecs(self):
        resp_message = self.ecs_api.stop_ecs(EcsApi().param_config["ecs_param"]["stop_ecs"])
        logging.warning(f"接口返回结果为{resp_message.json()}")
        try:
            assert resp_message.status_code == 200
            assert "RequestId" in resp_message.json()
        except Exception as e:
            raise e

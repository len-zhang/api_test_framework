# -*- coding:utf-8 -*-
from utils.logger import logger
import pytest
from api.ecs_api import EcsApi


class TestEcs:
    # def setup_class(self):
    #     self.ecs_api = EcsApi()
    #     logger.logger.info("=========执行setup_class==========")

    @pytest.mark.parametrize("param", [EcsApi().param_config["ecs_param"]["describe_ecs"]])
    def test_describe_ecs(self, resource_ready_destroy, param):
        resp_message = resource_ready_destroy[1].describe_ecs(param)
        try:
            assert resp_message.status_code == 200
        except Exception as e:
            raise e

    @pytest.mark.parametrize("param", EcsApi().param_config["ecs_param"]["update_ecs_name"])
    def test_update_ecs_name(self, resource_ready_destroy, param):
        logger.logger.info(f"原始yaml文件中的param为：{param}")
        if "InstanceId" in param.keys():
            param["InstanceId"] = resource_ready_destroy[0]
        else:
            logger.logger.error(f"param配置文件中没有找到InstanceId参数")
        logger.logger.info(f"替换后的yaml文件中param为：{param}")
        resp_message = resource_ready_destroy[1].update_ecs_name(param)
        try:
            assert resp_message.status_code == 200
            assert "RequestId" in resource_ready_destroy[1].json_data
        except Exception as e:
            raise e

    @pytest.mark.parametrize("param", [EcsApi().param_config["ecs_param"]["run_ecs"]])
    @pytest.mark.parametrize("json", [EcsApi().json_config["run_ecs"]])  # 多个参数化装饰器将用笛卡尔积方式组合数据
    def test_run_ecs(self, resource_ready_destroy, param, json):
        resp_message = resource_ready_destroy[1].run_ecs(param, json)
        result = resource_ready_destroy[1].get_jsonpath(expr="$.instanceIds[0]")
        logger.logger.warning(f"对返回json做jsonpath语法筛选后得到的值为{result}")
        try:
            assert resp_message.status_code == 200
            assert "ecs" in result[0]
        except Exception as e:
            raise e

    def test_delete_ecs(self, resource_ready_destroy):
        resp_message = resource_ready_destroy[1].delete_ecs(EcsApi().param_config["ecs_param"]["delete_ecs"])
        logger.logger.warning(f"接口返回结果为{resp_message.json()}")
        try:
            assert resp_message.status_code == 200
            assert "RequestId" in resp_message.json()
        except Exception as e:
            raise e

    def test_stop_ecs(self, resource_ready_destroy):
        resp_message = resource_ready_destroy[1].stop_ecs(EcsApi().param_config["ecs_param"]["stop_ecs"])
        logger.logger.warning(f"接口返回结果为{resp_message.json()}")
        try:
            assert resp_message.status_code == 200
            assert "RequestId" in resp_message.json()
        except Exception as e:
            raise e

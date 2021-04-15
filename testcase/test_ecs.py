# -*- coding:utf-8 -*-
import logging
import pytest
from api.ecs_api import EcsApi


class TestEcs:
    def setup_class(self):
        self.ecs_api = EcsApi()

    @pytest.mark.parametrize("param", [EcsApi().param_config["ecs_param"]["describe_ecs"]])
    def test_describe_ecs(self, param):
        resp_message = self.ecs_api.describe_ecs(param)
        try:
            assert resp_message.status_code == 200
        except Exception as e:
            raise e

    @pytest.mark.parametrize("param", EcsApi().param_config["ecs_param"]["update_ecs_name"])
    def test_update_ecs_name(self, param):
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

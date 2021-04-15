# -*- coding:utf-8 -*-
import pytest
from api.ebs_api import EbsApi


class TestEbs:
    def setup_class(self):
        self.ebs_api = EbsApi()

    # def test_add_member(self):
    #     resp_message = self.ebs_api.add_member()
    #     assert resp_message["errcode"] == 0

    @pytest.mark.parametrize("param", [EbsApi().param_config["ebs_param"]["describe_ebs"]])
    def test_describe_ebs(self, param):
        resp_message = self.ebs_api.describe_ebs(param)
        print(resp_message)
        try:
            assert resp_message.json()["total"] == 2
            assert resp_message.status_code == 200
        except Exception as e:
            raise e

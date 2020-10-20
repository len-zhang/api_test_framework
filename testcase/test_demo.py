# -*- coding:utf-8 -*-
import os
from api.address_api import AddressApi

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class TestDemo:
    def setup_class(self):
        self.address_api = AddressApi()

    def test_add_member(self):
        resp_message = self.address_api.add_member()
        assert resp_message["errcode"] == 0

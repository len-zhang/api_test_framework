# -*- coding:utf-8 -*-
import json
import requests
import logging

from jsonpath import jsonpath


class BaseApi:
    json_data = None

    def send_api(self, data: dict):
        logging.info(f"传给send_api的原始data数据为：{json.dumps(data, indent=4)}")
        r = requests.request(**data)
        logging.warning(f"发送接口的请求url为：{r.url}")
        logging.warning(f"发送接口的返回原始数据为：{r.text}")
        return r

    def get_jsonpath(self, expr):
        return jsonpath(self.json_data, expr)  # jsonpath返回的值是个list集合，精准匹配到的值都放入list中

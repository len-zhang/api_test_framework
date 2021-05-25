# -*- coding:utf-8 -*-
import json
import requests
from utils.logger import logger
from jsonpath import jsonpath


class BaseApi:
    json_data = None

    def send_api(self, data: dict):
        logger.logger.info(f"传给send_api的原始data数据为：{json.dumps(data, indent=4, ensure_ascii=False)}")
        r = requests.request(**data)
        logger.logger.warning(f"发送接口的请求url为：{r.url}")
        logger.logger.warning(f"发送接口的返回原始数据为：{r.text}")
        return r

    def get_jsonpath(self, expr):
        return jsonpath(self.json_data, expr)  # jsonpath返回的值是个list集合，精准匹配到的值都放入list中

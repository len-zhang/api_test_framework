# -*- coding:utf-8 -*-
import logging
import os
import base64
import hmac
from hashlib import sha1
import urllib.parse
import yaml

from api.base_api import BaseApi

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class WeworkUtils(BaseApi):
    def get_token(self, secret_id):
        corpid = "ww90db737a195a0094"
        corpsecret = secret_id
        token_dict = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        token = self.send_api(token_dict).json()["access_token"]
        return token


class MakeSignature:
    """
    生成OpenAPI需要的signature
    """

    def get_url(self, method, param, aks):
        url_list = []
        new_param = dict(param)  # 不能直接将param赋值给new_param，而是将param的值赋给new_param
        for i in new_param.keys():  # 检查传入param中每个key对应的value是否有中文，有的话转成url编码
            inc_ch: bool = MakeSignature().is_chinese(new_param[i])
            if inc_ch is True:
                new_param[i] = MakeSignature().url_encode(new_param[i])
            else:
                pass
        logging.info(f"**************原来的param没变****************仍然是{param}")
        logging.info(f"完成中文url编码后的param为{new_param}")
        if isinstance(new_param, dict):
            param_key = sorted(new_param.keys())  # 按照字典的key来排序，得到param_key是个list
            for i in param_key:
                intermediate_str = str(i) + '=' + str(new_param[i])
                url_list.append(intermediate_str)
        CanonicalizedQueryString = '&'.join(url_list)
        logging.info(f"完成排序后的字符串为{CanonicalizedQueryString}")
        StringToSign = method + '&' + MakeSignature.url_encode(self, "/") + '&' + MakeSignature.url_encode(self,
                                                                                                           CanonicalizedQueryString)
        logging.info(f"完成url编码后的字符串为{StringToSign}")
        signature = MakeSignature.HmacSHA1Encrypt(self, StringToSign, aks)
        logging.info(f"该接口生成的signature为：{signature}")
        param['Signature'] = signature
        return param

    def url_encode(self, url_str: str):
        new_str = urllib.parse.quote(url_str).replace("%2B", "%20").replace("/", "%2F").replace("%7E", "~")
        return new_str

    def HmacSHA1Encrypt(self, encrypt_text, encrypt_key):
        hmac_code = hmac.new(encrypt_key.encode(), encrypt_text.encode(), sha1).digest()
        return base64.b64encode(hmac_code).decode()

    def is_chinese(self, value: str):
        for ch in value:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False


class SetEnv:
    """
    从yaml中获取数据
    """

    @classmethod
    def get_url(cls):
        with open(f"{rootPath}/config/env.yaml", encoding="utf-8") as f:
            env_data = yaml.safe_load(f)
            return env_data

    @classmethod
    def get_param(cls):
        with open(f"{rootPath}/data/param.yaml", encoding="utf-8") as f:
            param_data = yaml.safe_load(f)
            return param_data

    @classmethod
    def get_json(cls):
        with open(f"{rootPath}/data/json.yaml", encoding="utf-8") as f:
            json_data = yaml.safe_load(f)
            return json_data


if __name__ == '__main__':
    # test = MakeSignature()
    # p1 = {"z-z_a.a~a a+a*a&a": "q1", "q-b_b.b~b b+b*b&b": "q2", "z-b_b.b~b b+b*b&b": "q3", "a-b_b.b~b b+b*b&b": "q4"}
    # p2 = {"Action": "DescribeEcs",
    #       "RegionId": "cn-tianjin-yfb",
    #       "Page": "1",
    #       "Size": "10",
    #       "AccessKeyId": "yzleTuvKgYmSBs8Z"}
    # k1 = "HD5yOp0Xc8FgaAkIz3i1z179a2xj26&"
    # print(test.get_url("GET", p2, k1))
    # body = {
    #     "period": 1,
    #     "payType": "YEAR_MONTH",
    #     "regionId": "cn-beijing",
    #     "azoneId": "cn-beijing-a",
    #     "vmSpecificationCode": "ecs.c5.medium",
    #     "sysDiskSpecificationCode": "ebs.hybrid.hdd",
    #     "sysDiskSize": "40",
    #     "bandWidthSpecificationCode": "eip.bgp.static",
    #     "bandWidthSize": 10,
    #     "imageId": "centos-imageTest-2",
    #     "imageSpecificationClassCode": "ecs.image.public",
    #     "vpcId": "vpc-9gbq0x14rj1ob",
    #     "securityGroupId": "sg-r1firmbmue2ob",
    #     "password": "qwer1234",
    #     "instanceName": "adsadda",
    #     "hostName": "",
    #     "baseQuantity": "1",
    #     "masterEniSubNetId": "deefbd1f8c684bdda00c82d72b20d7a6",
    #     "dataDisks": [
    #         {
    #             "dataDiskSpecificationCode": "ebs.hybrid.hdd",
    #             "dataDiskSize": 40
    #         }
    #     ]
    # }
    # with open(f"{rootPath}/data/json.yaml", 'a', encoding="utf-8") as f:
    #     f.write(yaml.dump(body))
    set_env = SetEnv
    print(set_env.get_param()["ecs_param"]["update_ecs_name"])
    # print(set_env.get_json()["run_ecs"])

# -*- coding:utf-8 -*-
import pytest
from api.ecs_api import EcsApi
from utils.logger import logger
import time

#  当一个方法上面加上@pytest.fixture() 装饰器就变成了fixture方法
#  yield能够激活fixture的teardown操作。yield相当于return
#  yield前面的操作相当于setup，yield语句后面相当于teardown操作
#  如果需要返回值，yield相当于return，直接写在yield后面即可

# 如果需要使用返回数据，则必须得把函数名放入到用例的传参中才行，单纯的autouse=True不行
from utils.utils import SetEnv


@pytest.fixture()
def resource_ready_destroy():
    time1 = 0
    time2 = 0
    ecs = EcsApi()
    ecs.run_ecs(EcsApi().param_config["ecs_param"]["run_ecs"], EcsApi().json_config["run_ecs"])
    ecs_name = ecs.get_jsonpath(expr="$.instanceIds[0]")
    logger.logger.debug(f"==========jsonpath获取到的实例id为{ecs_name}==========")
    logger.logger.info("==========等待查询主机列表接口可以返回主机信息==========")
    time.sleep(10)
    while True:
        ecs.describe_ecs(EcsApi().param_config["ecs_param"]["describe_ecs"])
        status = ecs.get_jsonpath(expr="$.list[0].status")
        logger.logger.info(f"检查主机实例当前的状态为{status}")
        if isinstance(status, list):
            if status[0] == 'RUNNING':
                break
            elif time1 == 18:
                logger.logger.error("创建主机3分钟仍然没有变为运行中状态！")
                break
            else:
                time.sleep(10)
                time1 += 1
                continue
        else:
            logger.logger.error("订单失败，没有下发到A层！")
            exit()
            break
    SetEnv.replace_param(ecs_name[0])  # 修改pram.yaml文件中的${ecs_name}
    yield ecs_name[0]
    logger.logger.info("=================进入用例后置步骤=================")
    result = ecs.stop_ecs(EcsApi().param_config["ecs_param"]["stop_ecs"]).status_code
    if result == 200:
        while True:
            ecs.describe_ecs(EcsApi().param_config["ecs_param"]["describe_ecs"])
            status = ecs.get_jsonpath(expr="$.list[0].status")
            logger.logger.info(f"检查主机实例当前的状态为{status}")
            if status[0] == 'DOWN':
                break
            elif time2 == 12:
                logger.logger.error("关闭主机1分钟仍然没有变为关停状态！")
                break
            else:
                time.sleep(5)
                time2 += 1
                continue
    else:
        logger.logger.error("关闭主机实例失败！")
        exit()
    ecs.delete_ecs(EcsApi().param_config["ecs_param"]["delete_ecs"])
    SetEnv.recovery_param()  # 将param.yaml恢复回带${ecs_name}的形式

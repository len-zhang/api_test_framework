# -*- coding:utf-8 -*-
import logging
import os
import time


class Logger(object):
    def __init__(self):
        self.init_logger()

    def init_logger(self, log_path=os.path.join(os.path.dirname(os.getcwd()), "log")):
        def get_timestamp():
            timestamp = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
            return timestamp

        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_path = os.path.join(log_path, "openapi_log_{}.txt".format(get_timestamp()))
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.DEBUG)
        handler = logging.FileHandler(log_path)
        # handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


logger = Logger()

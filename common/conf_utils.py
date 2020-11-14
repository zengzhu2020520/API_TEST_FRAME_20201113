#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: read_conf.py
# @time: 2020-11-14 17:55
# @desc:
import os
import configparser

conf_path_01 = os.path.join(os.path.dirname(__file__), '../conf/config.ini')


class ReadConfInfo(object):
    def __init__(self, conf_path=conf_path_01):
        self.read_conf = configparser.ConfigParser()
        self.read_conf.read(conf_path, encoding='utf-8')

    def read_configer(self, sec, option):
        conf_value = self.read_conf.get(sec, option)
        return conf_value

    @property
    def get_conf_URL(self):
        return self.read_configer('default', 'URL')

    @property
    def get_conf_CASE_DATA_PATH(self):
        return self.read_configer('path', 'CASE_DATA_PATH')


read_conf = ReadConfInfo()
if __name__ == '__main__':
    print(read_conf.get_conf_CASE_DATA_PATH)

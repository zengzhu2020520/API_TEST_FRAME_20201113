#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: read_excel.py
# @time: 2020-11-13 23:18
# @desc:
import xlrd3
import os
from common.excel_utils import ExcelUtils
from common.testdata_utils import TestDateUtils

excel_path = os.path.join(os.path.dirname(__file__), 'data/testdata.xlsx')

read_excel = ExcelUtils(excel_path, 'tag_testcase')
all_date = read_excel.get_all_excel_value_by_dict()


dict_01 = {}
for i in all_date:
    dict_01.setdefault(i['测试用例编号'], []).append(i)


listaa = []
for k, v in dict_01.items():
    # print(k)
    # print(v)
    dictb = {}
    dictb['case_name'] = k
    dictb['case_info'] = v
    listaa.append(dictb)
# print(listaa)
for i in listaa:
    print(i)

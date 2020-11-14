#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: testdata_utils.py
# @time: 2020-11-14 14:38
# @desc:
import os
from common.excel_utils import ExcelUtils

data_path = os.path.join(os.path.dirname(__file__), '../data/testdata.xlsx')


class TestDateUtils:
    def __init__(self, data_path=data_path, sheet_name='tag_testcase'):
        self.data_path = data_path
        self.sheet_name = sheet_name
        self.test_data = ExcelUtils(self.data_path, self.sheet_name).get_all_excel_value_by_dict()
        # print(self.test_data)

    def __get_excel_date_dict(self):
        test_case_list = {}
        for row_data in self.test_data:
            test_case_list.setdefault(row_data['测试用例编号'], []).append(row_data)
        return test_case_list

    def get_testcase_data(self):
        testcase_list = []
        all_date = self.__get_excel_date_dict()
        for k, v in all_date.items():
            one_case_dict = {}
            one_case_dict['case_name'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__ == '__main__':
    read = TestDateUtils()
    print(read.get_testcase_data())

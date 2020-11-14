#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: excel_utils.py
# @time: 2020-11-14 9:20
import os

import xlrd3


class ExcelUtils:
    def __init__(self, sheet_path, sheet_name):
        self.sheet_path = sheet_path
        self.sheet_name = sheet_name
        workbook = xlrd3.open_workbook(self.sheet_path)
        self.sheet = workbook.sheet_by_name(self.sheet_name)

    def get_all_rows(self):
        return self.sheet.nrows

    def get_all_ncols(self):
        return self.sheet.ncols

    def __get_merged_cell_value(self):
        return self.sheet.merged_cells

    def is_merged(self, cell_row, cell_col):
        is_cell = 0
        for (s_row, e_row, s_col, e_col) in self.__get_merged_cell_value():
            if s_row <= cell_row < e_row:
                if s_col <= cell_col < e_col:
                    is_cell = [s_row, e_row, s_col, e_col]
                    break
                else:
                    is_cell = 0
            else:
                is_cell = 0
        return is_cell

    def get_singe_cell_value(self, cell_row, cell_col):
        cell_value = None
        for (s_row, e_row, s_col, e_col) in self.__get_merged_cell_value():
            if s_row <= cell_row < e_row:
                if s_col <= cell_col < e_col:
                    cell_value = self.sheet.cell_value(s_row, s_col)
                    break  # 防止循环
                else:
                    cell_value = self.sheet.cell_value(cell_row, cell_col)
            else:
                cell_value = self.sheet.cell_value(cell_row, cell_col)
        return cell_value

    def get_all_excel_value_by_dict(self):
        date_01 = []
        for i in range(1, self.sheet.nrows):
            date_02 = {}
            for j in range(self.sheet.ncols):
                date = self.get_singe_cell_value(i, j)
                date_02[self.sheet.cell_value(0, j)] = date
            date_01.append(date_02)
        return date_01


if __name__ == '__main__':
    data_path = os.path.join(os.path.dirname(__file__), '../samples/data/testdata.xlsx')
    read_excel = ExcelUtils(data_path, 'tag_testcase')
    data = read_excel.get_all_excel_value_by_dict()
    for i in data:
        print(i)

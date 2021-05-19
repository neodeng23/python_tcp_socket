# code:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import csv
import os
import sys


class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("Test_Item")  # 设置表格名称
        self.resize(1200, 800)  # 设置表格尺寸（整体大小）
        self.setColumnCount(5)  # 设置列数
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.scrollToBottom()
        # self.setColumnWidth(0, 400)  # 设置列宽(第几列， 宽度)
        # self.setRowHeight(0, 100)  # 设置行高(第几行， 行高)

        column_name = ["Time", "DUT", "Process", "CMD", "PLC"]
        self.setHorizontalHeaderLabels(column_name)  # 设置列名称

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setDefaultSectionSize(117)
        # self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:11pt '宋体';color: black;};")
        # "QHeaderView::section{background-color:rgb(40,143,218);font:13pt '宋体';color: white;};")

    def update_item_data(self, data):
        """
        实时向UI界面表格中更新数据，新增一行
        更新内容 data = ["Time", "DUT", "Process", "CMD", "PLC"]
        """
        num = self.rowCount()
        self.insertRow(num)
        for line_num in range(0, len(data)):
            self.setItem(num, line_num, QTableWidgetItem(data[line_num]))  # 设置表格内容(行， 列) 文字
        # self.change_res_color(data[0], num)

    def change_res_color(self, res, num):
        if res == "pass" or res == "All_Pass!!!!":
            self.item(num, 0).setBackground(QBrush(QColor(0, 255, 0)))
        elif res == "Running":
            self.item(num, 0).setBackground(QBrush(QColor(255, 255, 0)))
        else:
            self.item(num, 0).setBackground(QBrush(QColor(255, 0, 0)))  # 红色

    def update_item_data_without_add_new_line(self, data):
        """
        实时像UI界面表格中更新数据，更新在当前的最后一行，不新增行
        更新内容 data = ["Time", "DUT", "Process", "CMD", "PLC"]
        """
        num = self.rowCount()
        for line_num in range(0, len(data)):
            self.setItem(num - 1, line_num, QTableWidgetItem(data[line_num]))  # 设置表格内容(行， 列) 文字
        self.change_res_color(data[0], num - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyTable()
    mainWindow.show()
    sys.exit(app.exec_())
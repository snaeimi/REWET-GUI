# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 18:18:58 2022

@author: snaeimi
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from List_File_Open import Ui_list_file_open
import os
import pandas as pd

class List_File_Open_Designer(Ui_list_file_open):
    def __init__(self):
        self._window = QtWidgets.QDialog()
        self.setupUi(self._window)
        #self.
        self.current_path = os.getcwd()
        self.cur_repr_path = str(self.current_path)
        self.file_address_line.setText(self.cur_repr_path)
        self.list_table_data = None
        
        self.browse_button.clicked.connect(self.openFileDialog)
        self.column_combo.currentTextChanged.connect(self.currentColumnChangedByCombo)
        self.list_table.itemSelectionChanged.connect(self.listTableSelectionChanged)
        
    def openFileDialog(self):
        file_fialog_window = QtWidgets.QFileDialog()
        file_address = file_fialog_window.getOpenFileName(self._window, "Select File", self.cur_repr_path, "Excel 2007 File (*.xlsx)")
        
        if len(file_address[0]) < 1:
            return
        
        self.current_path = file_address[0]
        self.current_repr_path = str(file_address[0])
        
        i_read_successful = self.readExcelFile(self.current_path) 
        if i_read_successful == False:
            return
        
        self.list_table.clear()
        self.populateListTable()
    #def getAbsPlatformSpecificPath(self, path):
        #if ":":
            #path = path.split('/')[1:]
            
    def errorMSG(self, error_title, error_msg, error_more_msg=None):
        self.error_widget = QtWidgets.QMessageBox()
        self.error_widget.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_widget.setText(error_msg)
        self.error_widget.setWindowTitle(error_title)
        self.error_widget.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if error_more_msg!=None:
            self.error_widget.setInformativeText(error_more_msg)
        self.error_widget.exec_()
        
    def readExcelFile(self, path):
        temp = pd.read_excel(path)
        if temp.columns.is_unique == False:
            self.errorMSG("Opening File failed", 'The Headers are not unique')
            return False
        self.list_table_data = temp
        return True
    
    def populateListTable(self):
        i = 0
        
        self.list_table.setColumnCount(self.list_table_data.columns.size)
        self.list_table.setRowCount(self.list_table_data.index.size)
        print(self.list_table_data)
        j=0;
        for col_name  in self.list_table_data.columns:
            j += 1
            item = QtWidgets.QTableWidgetItem()
            item.setText(col_name)
            self.list_table.setHorizontalHeaderItem(j-1, item)
            
        for ind, row in self.list_table_data.iterrows():
            i += 1
            #self.list_table.insertRow(0)
            row_list = row.to_list()
            j = 0
            for item_text in row_list:
                j += 1
                item = QtWidgets.QTableWidgetItem(item_text)
                self.list_table.setItem(i-1, j-1, item)
        self.column_combo.clear()
        self.column_combo.addItems(self.list_table_data.columns.tolist())
        
    def currentColumnChangedByCombo(self):
        current_col      = self.column_combo.currentText()
        col_list         = self.list_table_data.columns.tolist()
        col_ind          = col_list.index(current_col)
        self.return_data = self.list_table_data[current_col].tolist()
        self.list_table.selectColumn(col_ind)
        
    def listTableSelectionChanged(self):
        current_col = self.list_table.selectedItems()
        if len(current_col) > 0:
            col_list    = self.list_table_data.columns.tolist()
            col_text     = col_list[current_col[0].column()]
            self.column_combo.setCurrentText(col_text)
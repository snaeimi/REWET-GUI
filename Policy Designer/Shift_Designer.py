# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:24:46 2022

@author: snaeimi
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
#from Policy import Shift
from Shift_Window import Ui_shift
#from Dialog_Box import errorMSG

class Shift_Designer(Ui_shift):
    def __init__(self, policy):
        self.policy = policy
        #super().__init__()
        self._window = QtWidgets.QDialog()
        #self.crew_window_ui = Ui_crew_window()
        self.setupUi(self._window)
        
        #self.populateTheCombos()
        self.InitializeShiftTable()
        self.add_button.clicked.connect(self.addShiftByButton)
        self.remove_button.clicked.connect(self.removeShiftByButton)
        self.shift_name_list.itemSelectionChanged.connect(self.shiftListItemChanged)
        self.shift_begining_list.itemSelectionChanged.connect(self.beginingTimeListItemChanged)
        self.shift_end_list.itemSelectionChanged.connect(self.endTimeListItemChanged)
        self.apply_button.clicked.connect(self.updateShiftIntoPolicy)
        self.apply_button.clicked.connect(self._window.accept)
        self.cancel_button.clicked.connect(self.cancelShiftData)
        self.cancel_button.clicked.connect(self._window.reject)
        self._window.closeEvent = self.override_closeEvent
        
        #self.pp.clicked.connect(self._window.close)
        #self.Add_crew_button.clicked.connect(self.addCrewTable)
        #self.add
        #self.crew_table.itemChanged.connect(self.crewTableItemChanged)
        #self.crew_table.mousePressEvent = self.override_crewTableMousePressEvent
        #self.crew_table.itemSelectionChanged.connect(self.crewTableSelectionChanged)
        #self._window.closeEvent = self.closeEvent

    
    def addShiftByButton(self):
        shift_name    = self.shift_name_line.text()
        begining_time = self.begining_time_input.time().hour()
        end_time      = self.end_time_input.time().hour()
        
        if begining_time >= end_time:
            self.errorMSG("Failed", "Error in Shift Time", "begining shoft time must be less than end shift time")
            return
        if len(shift_name) == 0:
            self.errorMSG("Failed", "Error in Shift name", "Shift name must be provided")
            return
        current_shift_name_list = [self.shift_name_list.item(i).text() for i in range(self.shift_name_list.count() ) ]
        if shift_name in current_shift_name_list:
            self.errorMSG("Failed","Duplicate shift name")
            return
        
        self.shift_name_list.addItem(shift_name)
        self.shift_begining_list.addItem(str(begining_time) )
        self.shift_end_list.addItem(str(end_time) )
        
    def errorMSG(self, error_title, error_msg, error_more_msg=None):
        self.error_widget = QtWidgets.QMessageBox()
        self.error_widget.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_widget.setText(error_msg)
        self.error_widget.setWindowTitle(error_title)
        self.error_widget.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if error_more_msg!=None:
            self.error_widget.setInformativeText(error_more_msg)
        self.error_widget.exec_()
        
    def InitializeShiftTable(self):
        shift_name_list     = self.policy.shift.index.to_list()
        shift_begining_list = self.policy.shift.begining.to_list()
        shift_end_list      = self.policy.shift.end.to_list()
        
        shift_begining_list = [str(time) for time in shift_begining_list]
        shift_end_list = [str(time) for time in shift_end_list]
        self.shift_name_list.addItems(shift_name_list)
        self.shift_begining_list.addItems(shift_begining_list)
        self.shift_end_list.addItems(shift_end_list)

    def shiftListItemChanged(self):
        item  = self.shift_name_list.selectedItems()
        if len(item) == 0:
            return
        item = item[0]
        
        index = -1
        current_shift_name_list = [self.shift_name_list.item(i).text() for i in range(self.shift_name_list.count() ) ]
        for i in range(self.shift_name_list.count()):
            if item.text() == current_shift_name_list[i]:
                index = i
                break
        self.shift_begining_list.setCurrentRow(index)
        self.shift_end_list.setCurrentRow(index)
        
    def beginingTimeListItemChanged(self):
        item  = self.shift_begining_list.selectedItems()
        if len(item) == 0:
            return
        item = item[0]
        index = -1
        current_shift_begining_time_list = [self.shift_begining_list.item(i) for i in range(self.shift_begining_list.count() ) ]
        for i in range(self.shift_begining_list.count()):
            if item == current_shift_begining_time_list[i]:
                index = i
                break
        self.shift_name_list.setCurrentRow(index)
        self.shift_end_list.setCurrentRow(index)
        
    def endTimeListItemChanged(self):
        item  = self.shift_end_list.selectedItems()
        if len(item) == 0:
            return
        item = item[0]
        
        index = -1
        current_shift_end_time_list = [self.shift_end_list.item(i) for i in range(self.shift_begining_list.count() ) ]
        for i in range(self.shift_end_list.count()):
            if item == current_shift_end_time_list[i]:
                index = i
                break
        self.shift_name_list.setCurrentRow(index)
        self.shift_begining_list.setCurrentRow(index)
        
    def removeShiftByButton(self):
        item  = self.shift_name_list.selectedItems()
        if len(item) == 0:
            return
        item = item[0]
        
        index = self.shift_name_list.row(item)
        
        self.shift_name_list.takeItem(index)
        self.shift_begining_list.takeItem(index)
        self.shift_end_list.takeItem(index)
        
    def updateShiftIntoPolicy(self):
        current_shift_name_list = [self.shift_name_list.item(i).text() for i in range(self.shift_name_list.count() ) ]
        current_shift_begining_time_list = [self.shift_begining_list.item(i).text() for i in range(self.shift_begining_list.count() ) ]
        current_shift_end_time_list = [self.shift_end_list.item(i).text() for i in range(self.shift_begining_list.count() ) ]
        
        begining_time_col = dict(zip(current_shift_name_list, current_shift_begining_time_list))
        end_time_col = dict(zip(current_shift_name_list, current_shift_end_time_list))
        
        shift_col = self.policy.shift.columns
        
        all_data = {shift_col[0]:begining_time_col, shift_col[1]:end_time_col}
        
        self.policy.shift = pd.DataFrame(all_data)
        
    def cancelShiftData(self):
        self.shift_name_list.clear()
        self.shift_begining_list.clear()
        self.shift_end_list.clear()
        self.InitializeShiftTable()
    
    def override_closeEvent(self, event):
        self.cancelShiftData()
        self._window.reject()
        event.accept()
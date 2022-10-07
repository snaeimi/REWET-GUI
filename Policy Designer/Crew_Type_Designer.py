# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:07:27 2022

@author: snaeimi
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from Crew_Type_Window import Ui_crew_type_window

class Crew_Type_Designer(Ui_crew_type_window):
    def __init__(self, policy):
        self.policy = policy
        self._window = QtWidgets.QDialog()
        self.setupUi(self._window)
        
        self.InitializeCrewTypeList()
        self.add_button.clicked.connect(self.addCrewTypeByButton)
        self.remove_button.clicked.connect(self.removeTypeByButton)
        self.apply_button.clicked.connect(self.updateCrewTypeIntoPolicy)
        self.apply_button.clicked.connect(self._window.accept)
        self.cancel_button.clicked.connect(self.cancelCrewTypeData)
        self.cancel_button.clicked.connect(self._window.reject)
        self._window.closeEvent = self.override_closeEvent
        #self.crew_type_list.itemSelectionChanged.connect(self.crewTypeListItemChanged)
        
        
    
    def addCrewTypeByButton(self):
        crew_type = self.crew_type_input.text()
        
        if len(crew_type) == 0:
            self.errorMSG("Failed", "Error in Shift name", "Shift name must be provided")
            return
        current_crew_type_list = [self.crew_type_list.item(i).text() for i in range(self.crew_type_list.count() ) ]
        if crew_type in current_crew_type_list:
            self.errorMSG("Failed", "Duplicate Crew type name")
            return
        
        self.crew_type_list.addItem(crew_type)

        
    def errorMSG(self, error_title, error_msg, error_more_msg=None):
        self.error_widget = QtWidgets.QMessageBox()
        self.error_widget.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_widget.setText(error_msg)
        self.error_widget.setWindowTitle(error_title)
        self.error_widget.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if error_more_msg!=None:
            self.error_widget.setInformativeText(error_more_msg)
        self.error_widget.exec_()
        
    def InitializeCrewTypeList(self):
        crew_type_list     = list(self.policy.crew_types)
        
        self.crew_type_list.addItems(crew_type_list)
                
    def removeTypeByButton(self):
        item  = self.crew_type_list.selectedItems()
        if len(item) == 0:
            return
        item = item[0]
        
        used_crew_types = [crew.definitions['crew_type'] for crew in self.policy.crew_data]
        if item.text() in used_crew_types:
            self.errorMSG("Failed", "The crew type is in use")
            return
        
        index = self.crew_type_list.row(item)
        
        self.crew_type_list.takeItem(index)
    
    def updateCrewTypeIntoPolicy(self):
        current_crew_type_list = [self.crew_type_list.item(i).text() for i in range(self.crew_type_list.count() ) ]
                
        self.policy.crew_types = set(current_crew_type_list)
        
    def cancelCrewTypeData(self):
        self.crew_type_list.clear()
        self.InitializeCrewTypeList()
    
    def override_closeEvent(self, event):
        self.cancelCrewTypeData()
        self._window.reject()
        event.accept()
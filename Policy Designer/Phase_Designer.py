# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:50:43 2022

@author: snaeimi
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import copy
from Phase_Window import Ui_Phase_Window

class Phase_Designer(Ui_Phase_Window):
    def __init__(self, policy):
        self.policy = policy
        
        self.sequence_copy = copy.deepcopy(policy.sequence)
        self._window = QtWidgets.QDialog()
        self.setupUi(self._window)
        self.element_list.currentItemChanged.connect(self.elementListItemChanged)
        #self.element_list.itemSelectionChanged.connect(self.crewTableSelectionChanged)
        self.current_element_type = None
        self.up_button.clicked.connect(self.upByButton)
        self.down_button.clicked.connect(self.downByButton)
        self.add_button.clicked.connect(self.addPhase)
        self.remove_button.clicked.connect(self.removeByButton)
        apply_button = self.buttons.button(QtWidgets.QDialogButtonBox.Apply)
        reset_button = self.buttons.button(QtWidgets.QDialogButtonBox.Reset)
        apply_button.clicked.connect(self.updatePolicyWithNewData)
        reset_button.clicked.connect(self.rejectNewData)
        self.buttons.rejected.connect(self.rejectNewData)
        self.buttons.accepted.connect(self.updatePolicyWithNewData)
        self.buttons.accepted.connect(self.phase_input.clear)
        self._window.closeEvent = self.closeEvent
        
    def addPhase(self):
        new_phase = self.phase_input.text()
        
        if new_phase == None or self.current_element_type==None:
            return
        elif len(new_phase) < 1:
            return
        elif new_phase in self.sequence_copy[self.current_element_type]:
            self.errorMSG('ERROR', 'Failed to add Phase!', 'Duplicate Phase name.')
            return
        
        self.sequence_copy[self.current_element_type].append(new_phase)
        self.phase_input.clear()
        self.populatePhaseList()
        
    def closeEvent(self, event):
        self.rejectNewData()
        event.accept()
        
    def elementListItemChanged(self, item):
        self.current_element_type = item.text()
        if  self.current_element_type == 'Distribution Node':
            self.current_element_type = 'DISTNODE'
        elif self.current_element_type == 'General Node':
            self.current_element_type = 'GNODE'
            
        self.current_element_type = self.current_element_type.upper()
        self.populatePhaseList()
    
    def errorMSG(self, error_title, error_msg, error_more_msg=None):
        self.error_widget = QtWidgets.QMessageBox()
        self.error_widget.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_widget.setText(error_msg)
        self.error_widget.setWindowTitle(error_title)
        self.error_widget.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if error_more_msg!=None:
            self.error_widget.setInformativeText(error_more_msg)
        self.error_widget.exec_()
    
    def getcurrentElementAndUpdate(self):
        return
        if len(self.element_list.selectedItems()) > 0:
            self.current_element_type = self.element_list.selectedItems()[0].text()
        
        return self.current_element_type
    
    def getPhaseDataDataForElementType(self, element_type):
        return self.sequence_copy[element_type]
    
    def populatePhaseList(self):
        if self.current_element_type == None:
            self.phase_list.clear()
            return
    
        #self.getcurrentElementAndUpdate()
        phase_data = self.getPhaseDataDataForElementType(self.current_element_type)
        self.phase_list.clear()
        self.showListInActionList(phase_data)
    
    def showListInActionList(self, input_list):
        self.phase_list.addItems(input_list)
        
    def upByButton(self):
        item  = self.phase_list.selectedItems()
        if len(item) == 0:
            return
        item = item[0]
        current_phase = item.text()
        
        phase_data = self.getPhaseDataDataForElementType(self.current_element_type)
        
        if len(phase_data) <= 1:
            return
        
        current_phase_index = phase_data.index(current_phase)
        
        if current_phase_index == 0:
            return
        
        phase_data.pop(current_phase_index)
        phase_data.insert(current_phase_index-1, current_phase)
        self.phase_list.clear()
        self.populatePhaseList()
        self.phase_list.setCurrentRow(current_phase_index-1)
    
    def downByButton(self):
        item  = self.phase_list.selectedItems()
        if len(item) == 0:
            return
        item = item[0]
        current_phase = item.text()
        
        phase_data = self.getPhaseDataDataForElementType(self.current_element_type)
        current_phase_index = phase_data.index(current_phase)
        if len(phase_data)-1 == current_phase_index:
            return
        
        phase_data.pop(current_phase_index)
        phase_data.insert(current_phase_index+1, current_phase)
        self.phase_list.clear()
        self.populatePhaseList()
        self.phase_list.setCurrentRow(current_phase_index+1)
        
    def removeByButton(self):
        item  = self.phase_list.selectedItems()
        if len(item) == 0:
            return
        item = item[0]
        current_phase = item.text()
        
        phase_data = self.getPhaseDataDataForElementType(self.current_element_type)
        current_phase_index = phase_data.index(current_phase)
                
        phase_data.pop(current_phase_index)
        self.phase_list.clear()
        self.populatePhaseList()
        
    def updatePolicyWithNewData(self):
        for element_type in self.sequence_copy:
            #new_data_list = self.sequence_copy[element_type]
            self.policy.sequence[element_type].clear()
            self.policy.sequence[element_type].extend(self.sequence_copy[element_type])
    
    def rejectNewData(self):
        self.sequence_copy = copy.deepcopy(self.policy.sequence)
        self.element_list.clearSelection()
        self.phase_list.clear()
        self.current_element_type = None
        self.phase_input.clear()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:13:23 2022

@author: snaeimi
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from Priority_Window import Ui_Priority_Window
from copy import deepcopy

class Priority_Designer(Ui_Priority_Window):
    def __init__(self, policy):
        self.priority = deepcopy(policy.priority)
        self._window = QtWidgets.QDialog()
        self.setupUi(self._window)
        
        self.poplateData()
        
        self.crew_type_list.currentRowChanged.connect(self.crewTypeSelectionChanged)
        self.damage_group_list.currentRowChanged.connect(self.prioritySelectionChanged)
        self.phase_list.currentRowChanged.connect(self.prioritySelectionChanged)
        self.secondary_list.currentRowChanged.connect(self.prioritySelectionChanged)
        self.remove_prioirty_button.clicked.connect(self.removePriorityByButton)
        self.up_prioirty_button.clicked.connect(self.upPriorityByButton)
        self.down_prioirty_button.clicked.connect(self.downPriorityByButton)
        #self.damage_group_list.currentItemChanged.connect(self.prioritySelectionChangedItem)
        #self.phase_list.currentItemChanged.connect(self.prioritySelectionChangedItem)
        #self.secondary_list.currentItemChanged.connect(self.prioritySelectionChangedItem)
        
    def poplateData(self):
        crew_type_list = []
        
        for crew_type in self.priority:
            crew_type_list.append(crew_type)

        if len(crew_type_list) < 1:
            return
        
        self.crew_type_list.addItems(crew_type_list)
        
        first_crew_type = crew_type_list[0]
        #self.populatePriority(first_crew_type)
    
    def populatePriority(self, current_type):
        crew_priority_data = self.priority[current_type]
        priority_data = crew_priority_data.loc[1]
        secondary_data = crew_priority_data.loc[2]
        if len(priority_data) != len(secondary_data):
            raise ValueError("There is an error in list length. Report it back to teh developers please")
        
        phase_list        = [item[0] for item in priority_data]
        damage_group_list = [item[1] for item in priority_data]
        
        
        self.damage_group_list.addItems(damage_group_list)
        self.phase_list.addItems(phase_list)
        self.secondary_list.addItems(secondary_data)
    
    def selectPriorityRow(self, row):
        self.damage_group_list.setCurrentRow(row)
        self.phase_list.setCurrentRow(row)
        self.secondary_list.setCurrentRow(row)

        if row < 0:
            self.remove_prioirty_button.setEnabled(False)
            return
        else:
            self.remove_prioirty_button.setEnabled(True)
            
        
        current_damage_group = self.damage_group_list.currentItem().text()
        current_phase        = self.phase_list.currentItem().text()
        secondary_priority   = self.secondary_list.currentItem().text()
        
        self.setCurrentCombos(current_damage_group, current_phase, secondary_priority)
    
    def crewTypeSelectionChanged(self, current_row):
        current_type = self.crew_type_list.currentItem().text()
        self.clearPriority()
        self.populatePriority(current_type)
    
    def prioritySelectionChanged(self, current_row):
        self.selectPriorityRow(current_row)
       
        
        
        count = self.damage_group_list.count()
        #print(current_row)
        #print("coun: "+str(count))
        if count < 2:
            self.up_prioirty_button.setEnabled(False)
            self.down_prioirty_button.setEnabled(False)
        else:
            self.up_prioirty_button.setEnabled(True)
            self.down_prioirty_button.setEnabled(True)
                
    
    #def prioritySelectionChangedItem(self, current_item, previous_item):
        #current_damage_group = current_item.te
        #(current_item)
        
    def setCurrentCombos(self, current_damage_group, current_phase, secondary_priority):
        self.damage_group_combo.setCurrentText(current_damage_group)
        self.phase_combo.setCurrentText(current_phase)
        self.secondary_combo.setCurrentText(secondary_priority)
    
    def removePriorityByButton(self):
        current_row = self.damage_group_list.currentRow()
        crew_type = self.crew_type_list.currentItem().text()
        crew_priority_data = self.priority[crew_type]
        priority_data = crew_priority_data.loc[1]
        secondary_data = crew_priority_data.loc[2]
        
        priority_data.pop(current_row)
        secondary_data.pop(current_row)
        self.clearPriority()
        self.populatePriority(crew_type)

        if current_row == self.damage_group_list.count():
            current_row = current_row -1
        
            
        self.selectPriorityRow(current_row)
        
    def upPriorityByButton(self):
        current_row = self.damage_group_list.currentRow()
        if current_row <= 0:
            return
        
        crew_type = self.crew_type_list.currentItem().text()
        crew_priority_data = self.priority[crew_type]
        priority_data = crew_priority_data.loc[1]
        secondary_data = crew_priority_data.loc[2]
        
        temp = priority_data[current_row]
        priority_data[current_row] = priority_data[current_row-1]
        priority_data[current_row-1] = temp
        self.clearPriority()
        self.populatePriority(crew_type)
        self.selectPriorityRow(current_row-1)
    
    def clearPriority(self):
        count = self.damage_group_list.count()
        for i in range(self.damage_group_list.count()):
            self.damage_group_list.takeItem(count-i-1)
            self.phase_list.takeItem(count-i-1)
            self.secondary_list.takeItem(count-i-1)
        
    def downPriorityByButton(self):
        current_row = self.damage_group_list.currentRow()
        count = self.damage_group_list.count()
        if current_row >= count-1:
            return
        
        crew_type = self.crew_type_list.currentItem().text()
        crew_priority_data = self.priority[crew_type]
        priority_data = crew_priority_data.loc[1]
        secondary_data = crew_priority_data.loc[2]
        temp = priority_data[current_row+1]
        priority_data[current_row+1] = priority_data[current_row]
        priority_data[current_row] = temp
        self.clearPriority()
        self.populatePriority(crew_type)
        self.selectPriorityRow(current_row+1)
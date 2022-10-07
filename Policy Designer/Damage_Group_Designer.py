# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 12:49:11 2022

@author: snaeimi
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from Damage_Group_Window import Ui_Damage_Group
from List_File_Open_Designer import List_File_Open_Designer
from copy import deepcopy

class Damage_Group_Designer(Ui_Damage_Group):
    def __init__(self, policy):
        self.entity = deepcopy(policy.entity)
        self.entity_rule = deepcopy(policy.entity_rule)
        self.condition_types={'PIPE':['ALL','LIST','DIAMETER'], 'NODE':['ALL','LIST', 'NUMBER OF DAMAGES'], 'PUMP':['ALL','LIST'], 'GENRAL NODE': ['ALL','LIST'],
                              'TANK':['ALL','LIST'], 'RESERVOIR':['ALL','LIST']}
        self.condition_list={'ALL':None, 'LIST':['INCLUDE IN', 'NOT INCLUDED'], 'DIAMETER':['bg','be','lt','le', 'eq','nq'], 'NUMBER OF DAMAGES':['bg','be','lt','le', 'eq','nq']}
        self.list_data = []
        #self.list_as_condition_value = False
        #self.sequence_copy = copy.deepcopy(policy.sequence)
        self._window = QtWidgets.QDialog()
        self.setupUi(self._window)
        
        self.populateDamageGroupList()
        self.listDataPopulate()
        
        self.damage_group_add_button.clicked.connect(self.addDamageGroupByButton)
        self.damage_group_edit_button.clicked.connect(self.editDamageGroupByButton)
        self.damage_group_remove_button.clicked.connect(self.removeDamageGroupByButton)
        self.move_list_value_button.clicked.connect(self.addListByButton)
        self.add_condition_button.clicked.connect(self.addConditionByButton)
        self.remove_condition_button.clicked.connect(self.removeConditionByButton)
        self.open_file_button.clicked.connect(self.openNewFileList)
        
        
        self.damage_group_table.itemSelectionChanged.connect(self.damageGroupTableItemChanged)
        self.condition_table.itemSelectionChanged.connect(self.conditionTableItemChanged)
        self.condition_type_combo.currentTextChanged.connect(self.conditionTypeComboChanged)
        self.condition_type_combo.currentTextChanged.connect(self.activateDeactivateAddButton)
        self.condition_value_line.textChanged.connect(self.activateDeactivateAddButton)
        
        #self._window.closeEvent = self.closeEvent
    
    def addConditionByButton(self):
        selected_damage_group_name = self.damage_group_table.item(self.selected_damage_location_row, 0).text()
        #element_type = self.entity[selected_damage_group_name]
        
        condition_type  = self.condition_type_combo.currentText()
        condition       = self.condition_combo.currentText()
        condition_value = self.condition_value_line.text()
        
        if condition_value == "--List--" and self.condition_value_line.isEnabled() == False:
            condition_value = self.list_data.copy()
         
        new_rule = (condition_type, condition, condition_value)
        if selected_damage_group_name in self.entity_rule:
            self.entity_rule[selected_damage_group_name].append(new_rule)
        else:
            self.entity_rule[selected_damage_group_name]=[]
            self.entity_rule[selected_damage_group_name].append(new_rule)
        
        self.clearConditionTable()
        self.populateConditionTable(selected_damage_group_name)
    
    def removeConditionByButton(self):
        items = self.condition_table.selectedItems()
        if len(items) < 1:
            return
        row_index = items[0].row()
        self.condition_table.removeRow(row_index)
        
    def addDamageGroupByButton(self):
        new_damage_group_name = self.name_line.text()
        if len(new_damage_group_name) < 1:
            return
        #elif new_damage_group_name in
        all_names = []
        for i in range(self.damage_group_table.rowCount()):
            all_names.append(self.damage_group_table.item(i,0).text())
        print(all_names)
        
        if new_damage_group_name in all_names:
            self.errorMSG("Error", 'Damage Group Not added!', 'Duplicate Damage Group Name.')
            return
            
        new_damage_group_element_type = self.element_combo.currentText()
        self.addDamageGroupRow(new_damage_group_name, new_damage_group_element_type)
    
    def activateDeactivateAddButton(self):
        con_type = self.condition_type_combo.currentText()
        con      = self.condition_combo.currentText()
        value    = self.condition_value_line.text()
        
        enable = False
        if con_type == "ALL":
            enable = True
        elif con_type == 'LIST' and len(self.list_data) > 0:
                enable = True
        elif con_type == 'DIAMETER' and len(value) > 0:
            enable = True
        self.add_condition_button.setEnabled(enable)    
        
    def addDamageGroupRow(self, name, element_type):
        number_of_rows = self.damage_group_table.rowCount()
        self.damage_group_table.insertRow(number_of_rows)
        _name    = QtWidgets.QTableWidgetItem(name)
        _element = QtWidgets.QTableWidgetItem(element_type)
        _name.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
        _element.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
        
        self.damage_group_table.setItem(number_of_rows, 0, _name)
        self.damage_group_table.setItem(number_of_rows, 1,  _element)
    
    def errorMSG(self, error_title, error_msg, error_more_msg=None):
        self.error_widget = QtWidgets.QMessageBox()
        self.error_widget.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_widget.setText(error_msg)
        self.error_widget.setWindowTitle(error_title)
        self.error_widget.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if error_more_msg!=None:
            self.error_widget.setInformativeText(error_more_msg)
        self.error_widget.exec_()
    
    def clearConditionTable(self):
        for i in range(self.condition_table.rowCount()):
            self.condition_table.removeRow(0)
    
    def conditionTableItemChanged(self):
        item = self.condition_table.selectedItems()
        if len(item) < 1:
            self.remove_condition_button.setEnabled(False)
            return
        row_index = item[0].row()
        self.remove_condition_button.setEnabled(True)
    
    def damageGroupTableItemChanged(self):
        item = self.damage_group_table.selectedItems()
        if len(item) < 1:
            self.damage_group_edit_button.setEnabled(False)
            self.damage_group_remove_button.setEnabled(False)
            self.selected_damage_location_row = None
            self.condition_type_combo.clear()
            self.condition_combo.clear()
            self.condition_value_line.clear()
            self.clearConditionTable()
            return
        row_index = item[0].row()
        self.damage_group_edit_button.setEnabled(True)
        self.damage_group_remove_button.setEnabled(True)
        self.selected_damage_location_row = row_index
        
        selected_damage_group_name = self.damage_group_table.item(row_index, 0).text()
        self.condition_type_combo.clear()
        self.condition_combo.clear()
        self.condition_value_line.clear()
        self.clearConditionTable()
        self.populateConditionTable(selected_damage_group_name)
        
        self.name_line.setText(selected_damage_group_name)
        selected_damage_element_type_name = self.damage_group_table.item(row_index, 1).text()
        self.element_combo.setCurrentText(selected_damage_element_type_name)
        self.updateConditionTypeCombo()
        
        #index  = self.damage_group_table.model().index(row_index, 0)
        #self.damage_group_table.selectionModel().select(index, QtCore.QItemSelectionModel.Select | QtCore.QItemSelectionModel.Current)
        #print("item changed " + str( ))
    
    def editDamageGroupByButton(self):
        if self.selected_damage_location_row == None:
            return
        selected_damage_group_name = self.damage_group_table.item(self.selected_damage_location_row, 0).text()
        selected_damage_element_type_name = self.damage_group_table.item(self.selected_damage_location_row, 1).text()
        
        edited_damage_group_name        = self.name_line.text()
        edited_damage_element_type_name =self.element_combo.currentText()
        
        if edited_damage_group_name == selected_damage_group_name and edited_damage_element_type_name == selected_damage_element_type_name:
            return
        elif edited_damage_element_type_name != selected_damage_element_type_name:
            self.errorMSG("Error", "Cannot edit Elelemnt Type")
            return
        
        current_name_item = self.damage_group_table.item(self.selected_damage_location_row, 0)
        current_name_item.setText(edited_damage_group_name)
        
    def removeDamageGroupByButton(self):
        if self.selected_damage_location_row == None:
            return
        item = self.damage_group_table.selectedItems()
        row_index = item[0].row()
        self.damage_group_table.removeRow(row_index)
    
    def updateConditionTypeCombo(self):
        selected_damage_element_type_name = self.damage_group_table.item(self.selected_damage_location_row, 1).text()
        if selected_damage_element_type_name == None:
            self.condition_type_combo.clear()
            return
        condition_type_list = self.condition_types[selected_damage_element_type_name]
        self.condition_type_combo.clear()
        self.condition_type_combo.addItems(condition_type_list)
        
    def conditionTypeComboChanged(self):
        condition_type = self.condition_type_combo.currentText()
        self.decideConditionValueLineEnabled(condition_type)
        self.decideListButtonEnabled(condition_type)
        print(condition_type)
        
        condition_list = None
        if len(condition_type)==0:
            self.condition_combo.clear()
        else:
            condition_list = self.condition_list[condition_type]
        if condition_list==None:
            self.condition_combo.clear()
        else:
            self.condition_combo.clear()
            self.condition_combo.addItems(condition_list)
    
    def decideConditionValueLineEnabled(self, condition_type):
        if condition_type==None or condition_type == 'ALL' or condition_type == 'LIST':
            self.condition_value_line.setEnabled(False)
        else:
            self.condition_value_line.setEnabled(True)
            
    def decideListButtonEnabled(self, condition_type):
        if condition_type == 'LIST':
            self.move_list_value_button.setEnabled(True)
        else:
            self.move_list_value_button.setEnabled(False)
    
    def openNewFileList(self):
        new_page_file = List_File_Open_Designer()
        return_value = new_page_file._window.exec_()
        #print(return_value)
        if return_value:
            self.list_data = new_page_file.return_data
        self.listDataPopulate()
    
    def listDataPopulate(self):
        self.list_data_table.clear()
        self.list_data_table.addItems(self.list_data)
        
    def populateConditionTable(self, damage_group_name):
        #self.condition_table.clear()
        if damage_group_name in self.entity_rule:
            rules_list = self.entity_rule[damage_group_name]
            print(rules_list)
            for rule in rules_list:
                self.addConditionRow(rule[0], rule[1], rule[2])
    
    def populateDamageGroupList(self):
        #self.damage_group_table.clear()
        for name in self.entity.keys():
            print(name)
            element_type = self.entity[name]
            self.addDamageGroupRow(name, element_type)
                
    def  addConditionRow(self, condition_type, condition, condition_value):
        number_of_rows = self.condition_table.rowCount()
        self.condition_table.insertRow(number_of_rows)
        condition_type_item  = QtWidgets.QTableWidgetItem(condition_type)
        condition_item       = QtWidgets.QTableWidgetItem(condition)
        if type(condition_value) == list:
            condition_value='--list--'
        condition_value_item = QtWidgets.QTableWidgetItem(condition_value)
        
        condition_type_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
        condition_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
        condition_value_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
         
        self.condition_table.setItem(number_of_rows, 0, condition_type_item)
        self.condition_table.setItem(number_of_rows, 1,  condition_item)
        self.condition_table.setItem(number_of_rows, 2,  condition_value_item)
    
    def addDamageGroupRow(self, name, element_type):
        number_of_rows = self.damage_group_table.rowCount()
        self.damage_group_table.insertRow(number_of_rows)
        
        name_item         = QtWidgets.QTableWidgetItem(name)
        element_type_item = QtWidgets.QTableWidgetItem(element_type)
        name_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
        element_type_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
        
        self.damage_group_table.setItem(number_of_rows, 0, name_item)
        self.damage_group_table.setItem(number_of_rows, 1, element_type_item)
    
    def addListByButton(self):
        #self.list_data.clear()
        #item_list = self.list_data_table.items()
        self.condition_value_line.setText('--List--')
        
    
        
        
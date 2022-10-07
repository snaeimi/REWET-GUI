# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:47:17 2022

@author: snaeimi
"""
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from Policy import Single_Crew
from crew_window import Ui_crew_window
from Shift_Designer import Shift_Designer
from Crew_Type_Designer import Crew_Type_Designer

class Crew_Designer(Ui_crew_window):
    def __init__(self, policy):
        self.policy = policy
        
        self._window = QtWidgets.QWidget()
        self.setupUi(self._window)
        
        self.shift_designer     = Shift_Designer(self.policy)
        self.crew_type_designer = Crew_Type_Designer(self.policy)
        
        self.populateTheCombos()
        self.InitializeTableCrew()
        self.add_shift_button.clicked.connect(self.saveTable)
        self.add_shift_button.clicked.connect(lambda    : self.show(self.shift_designer._window, 'shift'))
        self.add_crew_type_button.clicked.connect(self.saveTable)
        self.add_crew_type_button.clicked.connect(lambda: self.show(self.crew_type_designer._window, 'crew_type'))
        self.Add_crew_button.clicked.connect(self.addCrewTable)
        #self.add
        self.crew_table.itemChanged.connect(self.crewTableItemChanged)
        self.crew_table.mousePressEvent = self.override_crewTableMousePressEvent
        self.crew_table.itemSelectionChanged.connect(self.crewTableSelectionChanged)
        self._window.closeEvent = self.closeEvent
#class Add_Crew(QtWidgets.QWidget):
    
    def show(self, func, dialog_type):
        return_value = func.exec_()
        if return_value == 0:
            return
        if dialog_type == 'shift':
            self.updateCrewShift()
        elif dialog_type == 'crew_type':
            self.updateCrewType()
    
    def addCrewTable(self):
        crew_name  = self.Crew_name_text.text()
        crew_type  = self.crew_type_combo.currentText()
        base_x     = self.base_x_text.text()
        base_y     = self.base_y_text.text()
        cur_x      = self.cur_x_text.text()
        cur_y      = self.cur_y_text.text()
        crew_shift = self.shift_combo.currentText()

        if len(crew_name) == 0:
            crew_name = self.guessNewCrewName(crew_type)
        
        if not self.isTextFloatable(base_x):
            self.error('Error' ,'Base X must be a number (X Coordination)')
            return
        
        if not self.isTextFloatable(base_y):
            self.error('Error' ,'Base Y must be a number (Y Coordination)')
            return
        
        if not self.isTextFloatable(cur_x):
            self.error('Error' ,'Current X must be a number (X Coordination)')
            return
        
        if not self.isTextFloatable(cur_y):
            self.error('Error' ,'Current Y must be a number (Y Coordination)')
            return
        
        if crew_shift not in self.policy.shift.index:
            self.error('Error' ,'Shift name is not in shift list')
            return
        
        if crew_type not in self.policy.crew_types:
            self.error('Error' ,'Crew type is not in defined crew-type list')
            return
        self.populateTableRow(crew_name, crew_type, base_x, base_y, cur_x, cur_y, crew_shift)
    
    def closeEvent(self, event):
        self.saveTable()
        event.accept()
    
    def crewTableItemChanged(self, item):
        
        if item.column() == 0:
            same_name_list  = [self.crew_table.item(i, 0).text()  for i in range(self.crew_table.rowCount()) if self.crew_table.item(i, 0).text()==item.text()]
            if len(same_name_list) > 1:
                self.error('Error' ,'Crew name duplicate')
                item.setText(self.crew_table.last_value)
            
        if item.column() == 2:
            if not self.isTextFloatable(item.text()):
                self.error('Error' ,'Base X must be a number (X Coordination)')
                item.setText(self.crew_table.last_value)
        
        if item.column() == 3:
            if not self.isTextFloatable(item.text()):
                self.error('Error' ,'Base Y must be a number (Y Coordination)')
                item.setText(self.crew_table.last_value)
        
        if item.column() == 4:
            if not self.isTextFloatable(item.text()):
                self.error('Error' ,'cur. X must be a number (X Coordination)')
                item.setText(self.crew_table.last_value)
        
        if item.column() == 5:
            if not self.isTextFloatable(item.text()):
                self.error('Error' ,'cur. Y must be a number (Y Coordination)')
                item.setText(self.crew_table.last_value)
        
    def crewTableSelectionChanged(self):
        item = self.crew_table.selectedItems()
        if len(item) !=1:
            return
        self.crew_table.last_value = item[0].text()
    
    def InitializeTableCrew(self):
        for crew in self.policy.crew_data:
            crew_name  = crew['crew_name']
            crew_type  = crew['crew_type']
            base_x     = crew['cur_x']
            base_y     = crew['cur_y']
            cur_x      = crew['base_x']
            cur_y      = crew['base_y']
            crew_shift = crew['shift_name']
            self.populateTableRow(crew_name, crew_type, base_x, base_y, cur_x, cur_y, crew_shift)
            
    def isTextFloatable(self, text):
        try:
            float(text)
            return True
        except:
            return False

    def guessNewCrewName(self, crew_type):
        return crew_type+str(random.randint(0,1000))
        
    def error(self, error_title, error_msg):
        self.error_widget = QtWidgets.QMessageBox()
        self.error_widget.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_widget.setText(error_msg)
        self.error_widget.setWindowTitle(error_title)
        self.error_widget.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.error_widget.exec_()
        #self.error_widget.showMessage(error_msg)\        

    def populateTheCombos(self):
        
        crew_types = list(self.policy.crew_types)
        self.crew_type_combo.addItems(crew_types)
        
        shift_names = self.policy.shift.index.to_list()
        self.shift_combo.addItems(shift_names)
    
    def populateTableRow(self, crew_name, crew_type, base_x, base_y, cur_x, cur_y, crew_shift):
        number_of_rows = self.crew_table.rowCount()
        self.crew_table.insertRow(number_of_rows)
        self.crew_table.setItem(number_of_rows, 0, QtWidgets.QTableWidgetItem(crew_name) )
        self.crew_table.setItem(number_of_rows, 2, QtWidgets.QTableWidgetItem(base_x) )
        self.crew_table.setItem(number_of_rows, 3, QtWidgets.QTableWidgetItem(base_y) )
        self.crew_table.setItem(number_of_rows, 4, QtWidgets.QTableWidgetItem(cur_x) )
        self.crew_table.setItem(number_of_rows, 5, QtWidgets.QTableWidgetItem(cur_y) )
        
        crew_types  = list(self.policy.crew_types)
        crew_combo  = QtWidgets.QComboBox()
        crew_combo.addItems(crew_types)
        crew_combo.setCurrentText(crew_type)
        self.crew_table.setCellWidget(number_of_rows, 1, crew_combo)
        
        shift_names = self.policy.shift.index.to_list()
        shift_combo = QtWidgets.QComboBox()
        shift_combo.addItems(shift_names)
        shift_combo.setCurrentText(crew_shift)
        self.crew_table.setCellWidget(number_of_rows, 6, shift_combo)
        
    def saveTable(self):
        self.policy.crew_data.clear()
        
        for i in range(self.crew_table.rowCount()):
            crew_name  = self.crew_table.item(i, 0).text()
            crew_type  = self.crew_table.cellWidget(i, 1).currentText()
            base_x     = self.crew_table.item(i, 2).text()
            base_y     = self.crew_table.item(i, 3).text()
            cur_x      = self.crew_table.item(i, 4).text()
            cur_y      = self.crew_table.item(i, 5).text()
            crew_shift = self.crew_table.cellWidget(i, 6).currentText()
            new_crew = Single_Crew(crew_name, crew_type, float(base_x), float(base_y), float(cur_x), float(cur_y), crew_shift)
            
            self.policy.crew_data.append(new_crew)
    
    def override_crewTableMousePressEvent(self, mouseEvent):
        if mouseEvent.button() == QtCore.Qt.LeftButton:
            self.crew_table.clearSelection()
            mouse_position = QtGui.QCursor.pos()
            y      = self.crew_table.viewport().mapFromGlobal(mouse_position).y()
            x      = self.crew_table.viewport().mapFromGlobal(mouse_position).x()
            row    = self.crew_table.rowAt(y)
            column = self.crew_table.columnAt(x)
            index  = self.crew_table.model().index(row, column)
            self.crew_table.setCurrentCell(row, column)
            self.crew_table.selectionModel().select(index, QtCore.QItemSelectionModel.Select | QtCore.QItemSelectionModel.Current)
            
        if mouseEvent.button() == QtCore.Qt.RightButton:
            mouse_position = QtGui.QCursor.pos()
            y   = self.crew_table.viewport().mapFromGlobal(mouse_position).y()
            row = self.crew_table.rowAt(y)
            self.crew_table.selectRow(row)
            self.menu     = QtWidgets.QMenu(self._window)
            delete_action = QtWidgets.QAction('Delete', self._window)
            delete_action.triggered.connect(lambda: self.deleteTableRow(mouseEvent))
            self.menu.addAction(delete_action)
            self.menu.popup(mouse_position)
            
    def deleteTableRow(self, mouseEvent):
        mouse_position = QtGui.QCursor.pos()
        y   = self.crew_table.viewport().mapFromGlobal(mouse_position).y()
        row = self.crew_table.rowAt(y)
        self.crew_table.removeRow(row)
        
    def contextMenuEvent(self, event):
        self.menu    = QtWidgets.QMenu(self)
        delete_action = QtWidgets.QAction('Delete', self)
        delete_action.triggered.connect(lambda: self.deleteTableRow(event))
        self.menu.addAction(delete_action)
        # add other required actions
        self.menu.popup(QtGui.QCursor.pos())
    
    def updateCrewShift(self):
        self.shift_combo.clear()
        shift_names = self.policy.shift.index.to_list()
        self.shift_combo.addItems(shift_names)
        
        for i in range(self.crew_table.rowCount()):
            first_shift = self.crew_table.cellWidget(i, 6).currentText()
            self.crew_table.cellWidget(i, 6).clear()
            self.crew_table.cellWidget(i, 6).addItems(shift_names)
            self.crew_table.cellWidget(i, 6).setCurrentText(first_shift)
    
    def updateCrewType(self):
        self.crew_type_combo.clear()
        crew_type = list(self.policy.crew_types)
        self.crew_type_combo.addItems(crew_type)
        
        for i in range(self.crew_table.rowCount()):
            first_type = self.crew_table.cellWidget(i, 1).currentText()
            self.crew_table.cellWidget(i, 1).clear()
            self.crew_table.cellWidget(i, 1).addItems(crew_type)
            self.crew_table.cellWidget(i, 1).setCurrentText(first_type)
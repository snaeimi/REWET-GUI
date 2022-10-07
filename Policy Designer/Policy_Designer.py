# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:13:01 2022

@author: snaeimi
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import Ui_MainWindow
from Crew_Designer import Crew_Designer
from Phase_Designer import Phase_Designer
from Damage_Group_Designer import Damage_Group_Designer
from Priority_Designer import Priority_Designer
from Policy import Policy

class Policy_Designer(Ui_MainWindow):
    def __init__(self):
        #super().__init__()
        self.policy = Policy()
        self.policy.fakeUp()
        self.asli_app = QtWidgets.QApplication([])
        self.asli_MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.asli_MainWindow)
        #Other Windows Initialization
        self.crew_designer  = Crew_Designer(self.policy)
        
        self.phase_designer = Phase_Designer(self.policy)
        self.addButtonFunctionality()
    
    def run(self):
        self.asli_MainWindow.show()
        sys.exit(self.asli_app.exec_())
        
    def addButtonFunctionality(self):
        self.crew_button.clicked.connect(self.crewPageShow)
        self.damage_group_window.clicked.connect(self.damageGroupPageShow)
        self.phase_button.clicked.connect(self.phasePageShow)
        self.priority_button.clicked.connect(self.prioirtyPageShow)
        
    #def InitializeCrewWindow(self):
        
        
    def crewPageShow(self):
        self.crew_designer._window.show()
        #crew_window.exec_()
    
    def damageGroupPageShow(self):
        damage_group_designer = Damage_Group_Designer(self.policy)
        return_value = damage_group_designer._window.exec_()
        if return_value == True:
            self.policy.entity = damage_group_designer.entity
            self.policy.entity_rule = damage_group_designer.entity_rule
    
    def phasePageShow(self):
        self.phase_designer._window.show()
    
    def prioirtyPageShow(self):
        priority_designer_window = Priority_Designer(self.policy)
        return_value = priority_designer_window._window.exec_()
        if return_value == True:
            pass
        
if __name__ == "__main__":
    pdesigner = Policy_Designer()
    pdesigner.run()
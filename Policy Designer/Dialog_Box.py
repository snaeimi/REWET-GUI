# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:33:09 2022

@author: snaeimi
"""

from PyQt5 import QtCore, QtGui, QtWidgets

def errorMSG(self, error_title, error_msg, error_more_msg=None):
    self.error_widget = QtWidgets.QMessageBox()
    self.error_widget.setIcon(QtWidgets.QMessageBox.Critical)
    self.error_widget.setText(error_msg)
    self.error_widget.setWindowTitle(error_title)
    self.error_widget.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if error_more_msg!=None:
        self.error_widget.setDetailedText(error_more_msg)
    self.error_widget.exec_()
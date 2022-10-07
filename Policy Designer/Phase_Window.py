# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phase_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Phase_Window(object):
    def setupUi(self, Phase_Window):
        Phase_Window.setObjectName("Phase_Window")
        Phase_Window.resize(440, 300)
        Phase_Window.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttons = QtWidgets.QDialogButtonBox(Phase_Window)
        self.buttons.setGeometry(QtCore.QRect(70, 230, 291, 51))
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttons.setObjectName("buttons")
        self.element_list = QtWidgets.QListWidget(Phase_Window)
        self.element_list.setGeometry(QtCore.QRect(20, 30, 181, 111))
        self.element_list.setObjectName("element_list")
        item = QtWidgets.QListWidgetItem()
        self.element_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.element_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.element_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.element_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.element_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.element_list.addItem(item)
        self.phase_list = QtWidgets.QListWidget(Phase_Window)
        self.phase_list.setGeometry(QtCore.QRect(220, 30, 151, 192))
        self.phase_list.setObjectName("phase_list")
        self.phase_input = QtWidgets.QLineEdit(Phase_Window)
        self.phase_input.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.phase_input.setObjectName("phase_input")
        self.add_button = QtWidgets.QPushButton(Phase_Window)
        self.add_button.setGeometry(QtCore.QRect(150, 160, 51, 23))
        self.add_button.setObjectName("add_button")
        self.up_button = QtWidgets.QPushButton(Phase_Window)
        self.up_button.setGeometry(QtCore.QRect(380, 30, 40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.up_button.setFont(font)
        self.up_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.up_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/interface/icons/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_button.setIcon(icon)
        self.up_button.setIconSize(QtCore.QSize(35, 35))
        self.up_button.setObjectName("up_button")
        self.down_button = QtWidgets.QPushButton(Phase_Window)
        self.down_button.setGeometry(QtCore.QRect(380, 80, 40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.down_button.setFont(font)
        self.down_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/interface/icons/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_button.setIcon(icon1)
        self.down_button.setIconSize(QtCore.QSize(35, 35))
        self.down_button.setObjectName("down_button")
        self.remove_button = QtWidgets.QPushButton(Phase_Window)
        self.remove_button.setGeometry(QtCore.QRect(380, 130, 40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.remove_button.setFont(font)
        self.remove_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/interface/icons/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_button.setIcon(icon2)
        self.remove_button.setIconSize(QtCore.QSize(35, 35))
        self.remove_button.setObjectName("remove_button")

        self.retranslateUi(Phase_Window)
        self.buttons.accepted.connect(Phase_Window.accept)
        self.buttons.rejected.connect(Phase_Window.reject)
        QtCore.QMetaObject.connectSlotsByName(Phase_Window)

    def retranslateUi(self, Phase_Window):
        _translate = QtCore.QCoreApplication.translate
        Phase_Window.setWindowTitle(_translate("Phase_Window", "Phase"))
        __sortingEnabled = self.element_list.isSortingEnabled()
        self.element_list.setSortingEnabled(False)
        item = self.element_list.item(0)
        item.setText(_translate("Phase_Window", "Pipe"))
        item = self.element_list.item(1)
        item.setText(_translate("Phase_Window", "Distribution Node"))
        item = self.element_list.item(2)
        item.setText(_translate("Phase_Window", "Tank"))
        item = self.element_list.item(3)
        item.setText(_translate("Phase_Window", "Pump"))
        item = self.element_list.item(4)
        item.setText(_translate("Phase_Window", "Reservoir"))
        item = self.element_list.item(5)
        item.setText(_translate("Phase_Window", "General Node"))
        self.element_list.setSortingEnabled(__sortingEnabled)
        self.add_button.setText(_translate("Phase_Window", "Add"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Phase_Window = QtWidgets.QDialog()
    ui = Ui_Phase_Window()
    ui.setupUi(Phase_Window)
    Phase_Window.show()
    sys.exit(app.exec_())

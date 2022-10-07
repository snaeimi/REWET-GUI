# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'priority_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Priority_Window(object):
    def setupUi(self, Priority_Window):
        Priority_Window.setObjectName("Priority_Window")
        Priority_Window.resize(751, 488)
        self.groupBox = QtWidgets.QGroupBox(Priority_Window)
        self.groupBox.setGeometry(QtCore.QRect(230, 60, 241, 351))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.label_2.setObjectName("label_2")
        self.damage_group_combo = QtWidgets.QComboBox(self.groupBox)
        self.damage_group_combo.setGeometry(QtCore.QRect(10, 50, 101, 22))
        self.damage_group_combo.setObjectName("damage_group_combo")
        self.damage_group_list = QtWidgets.QListWidget(self.groupBox)
        self.damage_group_list.setGeometry(QtCore.QRect(10, 90, 101, 251))
        self.damage_group_list.setObjectName("damage_group_list")
        self.phase_list = QtWidgets.QListWidget(self.groupBox)
        self.phase_list.setGeometry(QtCore.QRect(120, 90, 101, 251))
        self.phase_list.setObjectName("phase_list")
        self.phase_combo = QtWidgets.QComboBox(self.groupBox)
        self.phase_combo.setGeometry(QtCore.QRect(120, 50, 101, 22))
        self.phase_combo.setObjectName("phase_combo")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 20, 61, 20))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Priority_Window)
        self.groupBox_2.setGeometry(QtCore.QRect(480, 60, 161, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 71, 20))
        self.label_6.setObjectName("label_6")
        self.secondary_combo = QtWidgets.QComboBox(self.groupBox_2)
        self.secondary_combo.setGeometry(QtCore.QRect(20, 50, 131, 22))
        self.secondary_combo.setObjectName("secondary_combo")
        self.secondary_list = QtWidgets.QListWidget(self.groupBox_2)
        self.secondary_list.setGeometry(QtCore.QRect(20, 90, 131, 251))
        self.secondary_list.setObjectName("secondary_list")
        self.add_prioirty_button = QtWidgets.QPushButton(Priority_Window)
        self.add_prioirty_button.setGeometry(QtCore.QRect(660, 110, 75, 23))
        self.add_prioirty_button.setObjectName("add_prioirty_button")
        self.remove_prioirty_button = QtWidgets.QPushButton(Priority_Window)
        self.remove_prioirty_button.setGeometry(QtCore.QRect(660, 170, 75, 23))
        self.remove_prioirty_button.setObjectName("remove_prioirty_button")
        self.edit_prioirty_button = QtWidgets.QPushButton(Priority_Window)
        self.edit_prioirty_button.setGeometry(QtCore.QRect(660, 140, 75, 23))
        self.edit_prioirty_button.setObjectName("edit_prioirty_button")
        self.up_prioirty_button = QtWidgets.QPushButton(Priority_Window)
        self.up_prioirty_button.setGeometry(QtCore.QRect(660, 240, 75, 23))
        self.up_prioirty_button.setObjectName("up_prioirty_button")
        self.down_prioirty_button = QtWidgets.QPushButton(Priority_Window)
        self.down_prioirty_button.setGeometry(QtCore.QRect(660, 270, 75, 23))
        self.down_prioirty_button.setObjectName("down_prioirty_button")
        self.groupBox_3 = QtWidgets.QGroupBox(Priority_Window)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 100, 161, 311))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 151, 20))
        self.label_5.setObjectName("label_5")
        self.crew_type_list = QtWidgets.QListWidget(Priority_Window)
        self.crew_type_list.setGeometry(QtCore.QRect(70, 150, 141, 251))
        self.crew_type_list.setObjectName("crew_type_list")
        self.buttonBox = QtWidgets.QDialogButtonBox(Priority_Window)
        self.buttonBox.setGeometry(QtCore.QRect(280, 430, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Priority_Window)
        self.buttonBox.accepted.connect(Priority_Window.accept)
        QtCore.QMetaObject.connectSlotsByName(Priority_Window)

    def retranslateUi(self, Priority_Window):
        _translate = QtCore.QCoreApplication.translate
        Priority_Window.setWindowTitle(_translate("Priority_Window", "Priority"))
        self.groupBox.setTitle(_translate("Priority_Window", "Primary"))
        self.label_2.setText(_translate("Priority_Window", "Damage Group"))
        self.label.setText(_translate("Priority_Window", "Phase"))
        self.groupBox_2.setTitle(_translate("Priority_Window", "Secondary"))
        self.label_6.setText(_translate("Priority_Window", "Distance"))
        self.add_prioirty_button.setText(_translate("Priority_Window", "Add"))
        self.remove_prioirty_button.setText(_translate("Priority_Window", "Remove"))
        self.edit_prioirty_button.setText(_translate("Priority_Window", "Edit"))
        self.up_prioirty_button.setText(_translate("Priority_Window", "Up"))
        self.down_prioirty_button.setText(_translate("Priority_Window", "Down"))
        self.groupBox_3.setTitle(_translate("Priority_Window", "Crew Type"))
        self.label_5.setText(_translate("Priority_Window", "Choose Crew Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Priority_Window = QtWidgets.QDialog()
    ui = Ui_Priority_Window()
    ui.setupUi(Priority_Window)
    Priority_Window.show()
    sys.exit(app.exec_())

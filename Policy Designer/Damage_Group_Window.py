# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'damage_group.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Damage_Group(object):
    def setupUi(self, Damage_Group):
        Damage_Group.setObjectName("Damage_Group")
        Damage_Group.resize(1021, 432)
        self.label_4 = QtWidgets.QLabel(Damage_Group)
        self.label_4.setGeometry(QtCore.QRect(400, 50, 101, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Damage_Group)
        self.label_5.setGeometry(QtCore.QRect(510, 50, 91, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Damage_Group)
        self.label_6.setGeometry(QtCore.QRect(620, 50, 81, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.condition_type_combo = QtWidgets.QComboBox(Damage_Group)
        self.condition_type_combo.setGeometry(QtCore.QRect(400, 70, 101, 22))
        self.condition_type_combo.setObjectName("condition_type_combo")
        self.condition_combo = QtWidgets.QComboBox(Damage_Group)
        self.condition_combo.setGeometry(QtCore.QRect(500, 70, 101, 22))
        self.condition_combo.setObjectName("condition_combo")
        self.condition_value_line = QtWidgets.QLineEdit(Damage_Group)
        self.condition_value_line.setEnabled(False)
        self.condition_value_line.setGeometry(QtCore.QRect(600, 70, 121, 22))
        self.condition_value_line.setClearButtonEnabled(False)
        self.condition_value_line.setObjectName("condition_value_line")
        self.condition_table = QtWidgets.QTableWidget(Damage_Group)
        self.condition_table.setGeometry(QtCore.QRect(400, 100, 321, 261))
        self.condition_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.condition_table.setObjectName("condition_table")
        self.condition_table.setColumnCount(3)
        self.condition_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(2, item)
        self.condition_table.horizontalHeader().setCascadingSectionResizes(False)
        self.condition_table.horizontalHeader().setDefaultSectionSize(100)
        self.condition_table.horizontalHeader().setHighlightSections(False)
        self.condition_table.horizontalHeader().setMinimumSectionSize(30)
        self.condition_table.horizontalHeader().setSortIndicatorShown(False)
        self.condition_table.horizontalHeader().setStretchLastSection(True)
        self.condition_table.verticalHeader().setStretchLastSection(False)
        self.name_line = QtWidgets.QLineEdit(Damage_Group)
        self.name_line.setGeometry(QtCore.QRect(70, 40, 101, 21))
        self.name_line.setObjectName("name_line")
        self.damage_group_add_button = QtWidgets.QPushButton(Damage_Group)
        self.damage_group_add_button.setGeometry(QtCore.QRect(310, 40, 51, 21))
        self.damage_group_add_button.setObjectName("damage_group_add_button")
        self.add_condition_button = QtWidgets.QPushButton(Damage_Group)
        self.add_condition_button.setEnabled(False)
        self.add_condition_button.setGeometry(QtCore.QRect(730, 60, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_condition_button.setFont(font)
        self.add_condition_button.setObjectName("add_condition_button")
        self.element_combo = QtWidgets.QComboBox(Damage_Group)
        self.element_combo.setGeometry(QtCore.QRect(180, 40, 111, 21))
        self.element_combo.setObjectName("element_combo")
        self.element_combo.addItem("")
        self.element_combo.addItem("")
        self.element_combo.addItem("")
        self.element_combo.addItem("")
        self.element_combo.addItem("")
        self.element_combo.addItem("")
        self.damage_group_table = QtWidgets.QTableWidget(Damage_Group)
        self.damage_group_table.setGeometry(QtCore.QRect(70, 70, 231, 291))
        self.damage_group_table.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.damage_group_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.damage_group_table.setObjectName("damage_group_table")
        self.damage_group_table.setColumnCount(2)
        self.damage_group_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.damage_group_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_group_table.setHorizontalHeaderItem(1, item)
        self.damage_group_table.horizontalHeader().setStretchLastSection(True)
        self.damage_group_table.verticalHeader().setStretchLastSection(False)
        self.damage_group_remove_button = QtWidgets.QPushButton(Damage_Group)
        self.damage_group_remove_button.setEnabled(False)
        self.damage_group_remove_button.setGeometry(QtCore.QRect(310, 100, 51, 21))
        self.damage_group_remove_button.setObjectName("damage_group_remove_button")
        self.damage_group_edit_button = QtWidgets.QPushButton(Damage_Group)
        self.damage_group_edit_button.setEnabled(False)
        self.damage_group_edit_button.setGeometry(QtCore.QRect(310, 70, 51, 21))
        self.damage_group_edit_button.setObjectName("damage_group_edit_button")
        self.list_data_table = QtWidgets.QListWidget(Damage_Group)
        self.list_data_table.setGeometry(QtCore.QRect(820, 100, 101, 261))
        self.list_data_table.setObjectName("list_data_table")
        self.move_list_value_button = QtWidgets.QPushButton(Damage_Group)
        self.move_list_value_button.setEnabled(False)
        self.move_list_value_button.setGeometry(QtCore.QRect(730, 220, 81, 23))
        self.move_list_value_button.setObjectName("move_list_value_button")
        self.open_file_button = QtWidgets.QPushButton(Damage_Group)
        self.open_file_button.setGeometry(QtCore.QRect(820, 60, 101, 41))
        self.open_file_button.setObjectName("open_file_button")
        self.remove_condition_button = QtWidgets.QPushButton(Damage_Group)
        self.remove_condition_button.setEnabled(False)
        self.remove_condition_button.setGeometry(QtCore.QRect(730, 110, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.remove_condition_button.setFont(font)
        self.remove_condition_button.setObjectName("remove_condition_button")
        self.buttonBox = QtWidgets.QDialogButtonBox(Damage_Group)
        self.buttonBox.setGeometry(QtCore.QRect(410, 390, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Damage_Group)
        self.buttonBox.accepted.connect(Damage_Group.accept)
        self.buttonBox.rejected.connect(Damage_Group.reject)
        QtCore.QMetaObject.connectSlotsByName(Damage_Group)

    def retranslateUi(self, Damage_Group):
        _translate = QtCore.QCoreApplication.translate
        Damage_Group.setWindowTitle(_translate("Damage_Group", "Damage Group"))
        self.label_4.setText(_translate("Damage_Group", "Condition Type"))
        self.label_5.setText(_translate("Damage_Group", "Condition"))
        self.label_6.setText(_translate("Damage_Group", "Conditon Value"))
        item = self.condition_table.horizontalHeaderItem(0)
        item.setText(_translate("Damage_Group", "Condition Type"))
        item = self.condition_table.horizontalHeaderItem(1)
        item.setText(_translate("Damage_Group", "Condition"))
        item = self.condition_table.horizontalHeaderItem(2)
        item.setText(_translate("Damage_Group", "Condition Value"))
        self.damage_group_add_button.setText(_translate("Damage_Group", "add"))
        self.add_condition_button.setText(_translate("Damage_Group", "Add "))
        self.element_combo.setItemText(0, _translate("Damage_Group", "PIPE"))
        self.element_combo.setItemText(1, _translate("Damage_Group", "PUMP"))
        self.element_combo.setItemText(2, _translate("Damage_Group", "NODE"))
        self.element_combo.setItemText(3, _translate("Damage_Group", "TANK"))
        self.element_combo.setItemText(4, _translate("Damage_Group", "RESERVOIR"))
        self.element_combo.setItemText(5, _translate("Damage_Group", "GENERAL NODE"))
        item = self.damage_group_table.horizontalHeaderItem(0)
        item.setText(_translate("Damage_Group", "Name"))
        item = self.damage_group_table.horizontalHeaderItem(1)
        item.setText(_translate("Damage_Group", "Element Type"))
        self.damage_group_remove_button.setText(_translate("Damage_Group", "Remove"))
        self.damage_group_edit_button.setText(_translate("Damage_Group", "Edit"))
        self.move_list_value_button.setText(_translate("Damage_Group", "<----------"))
        self.open_file_button.setText(_translate("Damage_Group", "List By File"))
        self.remove_condition_button.setText(_translate("Damage_Group", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Damage_Group = QtWidgets.QDialog()
    ui = Ui_Damage_Group()
    ui.setupUi(Damage_Group)
    Damage_Group.show()
    sys.exit(app.exec_())

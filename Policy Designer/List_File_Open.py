# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'List_File_Open.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_list_file_open(object):
    def setupUi(self, list_file_open):
        list_file_open.setObjectName("list_file_open")
        list_file_open.resize(465, 317)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(list_file_open.sizePolicy().hasHeightForWidth())
        list_file_open.setSizePolicy(sizePolicy)
        list_file_open.setMinimumSize(QtCore.QSize(465, 0))
        list_file_open.setMaximumSize(QtCore.QSize(465, 16777215))
        self.layoutWidget = QtWidgets.QWidget(list_file_open)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 30, 457, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.file_address_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.file_address_line.setObjectName("file_address_line")
        self.gridLayout.addWidget(self.file_address_line, 0, 2, 1, 2)
        self.browse_button = QtWidgets.QPushButton(self.layoutWidget)
        self.browse_button.setObjectName("browse_button")
        self.gridLayout.addWidget(self.browse_button, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.column_combo = QtWidgets.QComboBox(self.layoutWidget)
        self.column_combo.setObjectName("column_combo")
        self.gridLayout.addWidget(self.column_combo, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.open_button = QtWidgets.QPushButton(self.layoutWidget)
        self.open_button.setObjectName("open_button")
        self.gridLayout.addWidget(self.open_button, 1, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)
        self.list_table = QtWidgets.QTableWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_table.sizePolicy().hasHeightForWidth())
        self.list_table.setSizePolicy(sizePolicy)
        self.list_table.setObjectName("list_table")
        self.list_table.setColumnCount(0)
        self.list_table.setRowCount(0)
        self.gridLayout.addWidget(self.list_table, 2, 1, 1, 5)
        self.ok_cancel_button = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.ok_cancel_button.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel_button.setObjectName("ok_cancel_button")
        self.gridLayout.addWidget(self.ok_cancel_button, 3, 1, 1, 5)

        self.retranslateUi(list_file_open)
        self.ok_cancel_button.rejected.connect(list_file_open.reject)
        self.ok_cancel_button.accepted.connect(list_file_open.accept)
        QtCore.QMetaObject.connectSlotsByName(list_file_open)

    def retranslateUi(self, list_file_open):
        _translate = QtCore.QCoreApplication.translate
        list_file_open.setWindowTitle(_translate("list_file_open", "Dialog"))
        self.label.setText(_translate("list_file_open", "File Address"))
        self.browse_button.setText(_translate("list_file_open", "Browse"))
        self.label_2.setText(_translate("list_file_open", "Select Column"))
        self.open_button.setText(_translate("list_file_open", "Open "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    list_file_open = QtWidgets.QDialog()
    ui = Ui_list_file_open()
    ui.setupUi(list_file_open)
    list_file_open.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crew.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_crew_window(object):
    def setupUi(self, crew_window):
        crew_window.setObjectName("crew_window")
        crew_window.setWindowModality(QtCore.Qt.ApplicationModal)
        crew_window.resize(930, 577)
        self.Add_crew_button = QtWidgets.QPushButton(crew_window)
        self.Add_crew_button.setGeometry(QtCore.QRect(720, 240, 92, 29))
        self.Add_crew_button.setObjectName("Add_crew_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(crew_window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 280, 811, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.crew_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.crew_table.setEnabled(True)
        self.crew_table.setObjectName("crew_table")
        self.crew_table.setColumnCount(7)
        self.crew_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.crew_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.crew_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.crew_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.crew_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.crew_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.crew_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.crew_table.setHorizontalHeaderItem(6, item)
        self.horizontalLayout.addWidget(self.crew_table)
        self.label = QtWidgets.QLabel(crew_window)
        self.label.setGeometry(QtCore.QRect(10, 20, 741, 81))
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.add_crew_type_button = QtWidgets.QPushButton(crew_window)
        self.add_crew_type_button.setGeometry(QtCore.QRect(10, 160, 141, 29))
        self.add_crew_type_button.setObjectName("add_crew_type_button")
        self.add_shift_button = QtWidgets.QPushButton(crew_window)
        self.add_shift_button.setGeometry(QtCore.QRect(160, 160, 141, 29))
        self.add_shift_button.setObjectName("add_shift_button")
        self.Crew_name_text = QtWidgets.QLineEdit(crew_window)
        self.Crew_name_text.setGeometry(QtCore.QRect(20, 240, 101, 27))
        self.Crew_name_text.setText("")
        self.Crew_name_text.setObjectName("Crew_name_text")
        self.base_x_text = QtWidgets.QLineEdit(crew_window)
        self.base_x_text.setGeometry(QtCore.QRect(230, 240, 91, 27))
        self.base_x_text.setObjectName("base_x_text")
        self.base_y_text = QtWidgets.QLineEdit(crew_window)
        self.base_y_text.setGeometry(QtCore.QRect(330, 240, 91, 27))
        self.base_y_text.setObjectName("base_y_text")
        self.cur_x_text = QtWidgets.QLineEdit(crew_window)
        self.cur_x_text.setGeometry(QtCore.QRect(430, 240, 91, 27))
        self.cur_x_text.setObjectName("cur_x_text")
        self.cur_y_text = QtWidgets.QLineEdit(crew_window)
        self.cur_y_text.setGeometry(QtCore.QRect(530, 240, 91, 27))
        self.cur_y_text.setObjectName("cur_y_text")
        self.crew_type_combo = QtWidgets.QComboBox(crew_window)
        self.crew_type_combo.setGeometry(QtCore.QRect(130, 240, 83, 27))
        self.crew_type_combo.setObjectName("crew_type_combo")
        self.shift_combo = QtWidgets.QComboBox(crew_window)
        self.shift_combo.setGeometry(QtCore.QRect(630, 240, 83, 27))
        self.shift_combo.setObjectName("shift_combo")

        self.retranslateUi(crew_window)
        QtCore.QMetaObject.connectSlotsByName(crew_window)

    def retranslateUi(self, crew_window):
        _translate = QtCore.QCoreApplication.translate
        crew_window.setWindowTitle(_translate("crew_window", "Crew"))
        self.Add_crew_button.setText(_translate("crew_window", "Add Crew"))
        item = self.crew_table.horizontalHeaderItem(0)
        item.setText(_translate("crew_window", "Crew Name"))
        item = self.crew_table.horizontalHeaderItem(1)
        item.setText(_translate("crew_window", "Crew Type"))
        item = self.crew_table.horizontalHeaderItem(2)
        item.setText(_translate("crew_window", "Base X"))
        item = self.crew_table.horizontalHeaderItem(3)
        item.setText(_translate("crew_window", "Base Y"))
        item = self.crew_table.horizontalHeaderItem(4)
        item.setText(_translate("crew_window", "Cur. X"))
        item = self.crew_table.horizontalHeaderItem(5)
        item.setText(_translate("crew_window", "Cur. Y"))
        item = self.crew_table.horizontalHeaderItem(6)
        item.setText(_translate("crew_window", "Shift"))
        self.label.setText(_translate("crew_window", "Crew are entered based on their type, base and current location and their shift name.If there are multiple crews with the same attributes, you can enter the quantity or enter the value mutiple times with quantity equal to 1."))
        self.add_crew_type_button.setText(_translate("crew_window", "Add Crew Type"))
        self.add_shift_button.setText(_translate("crew_window", "Add Shift"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    crew_window = QtWidgets.QWidget()
    ui = Ui_crew_window()
    ui.setupUi(crew_window)
    crew_window.show()
    sys.exit(app.exec_())

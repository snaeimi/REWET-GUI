# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shift_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shift(object):
    def setupUi(self, shift):
        shift.setObjectName("shift")
        shift.setWindowModality(QtCore.Qt.ApplicationModal)
        shift.resize(471, 286)
        self.shift_name_line = QtWidgets.QLineEdit(shift)
        self.shift_name_line.setGeometry(QtCore.QRect(40, 40, 113, 20))
        self.shift_name_line.setObjectName("shift_name_line")
        self.begining_time_input = QtWidgets.QTimeEdit(shift)
        self.begining_time_input.setGeometry(QtCore.QRect(170, 40, 61, 22))
        self.begining_time_input.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.begining_time_input.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.begining_time_input.setObjectName("begining_time_input")
        self.end_time_input = QtWidgets.QTimeEdit(shift)
        self.end_time_input.setGeometry(QtCore.QRect(260, 40, 61, 22))
        self.end_time_input.setWrapping(False)
        self.end_time_input.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(16, 0, 0)))
        self.end_time_input.setObjectName("end_time_input")
        self.shift_name_list = QtWidgets.QListWidget(shift)
        self.shift_name_list.setGeometry(QtCore.QRect(40, 70, 111, 191))
        self.shift_name_list.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.shift_name_list.setObjectName("shift_name_list")
        self.shift_begining_list = QtWidgets.QListWidget(shift)
        self.shift_begining_list.setGeometry(QtCore.QRect(170, 70, 61, 191))
        self.shift_begining_list.setObjectName("shift_begining_list")
        self.shift_end_list = QtWidgets.QListWidget(shift)
        self.shift_end_list.setGeometry(QtCore.QRect(260, 70, 61, 191))
        self.shift_end_list.setObjectName("shift_end_list")
        self.add_button = QtWidgets.QPushButton(shift)
        self.add_button.setGeometry(QtCore.QRect(350, 40, 92, 31))
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QPushButton(shift)
        self.remove_button.setGeometry(QtCore.QRect(350, 80, 92, 31))
        self.remove_button.setObjectName("remove_button")
        self.label = QtWidgets.QLabel(shift)
        self.label.setGeometry(QtCore.QRect(40, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(shift)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(shift)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(shift)
        self.label_4.setGeometry(QtCore.QRect(350, 210, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.apply_button = QtWidgets.QPushButton(shift)
        self.apply_button.setGeometry(QtCore.QRect(350, 120, 92, 31))
        self.apply_button.setObjectName("apply_button")
        self.cancel_button = QtWidgets.QPushButton(shift)
        self.cancel_button.setGeometry(QtCore.QRect(350, 160, 92, 31))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(shift)
        QtCore.QMetaObject.connectSlotsByName(shift)

    def retranslateUi(self, shift):
        _translate = QtCore.QCoreApplication.translate
        shift.setWindowTitle(_translate("shift", "Shift"))
        self.add_button.setText(_translate("shift", "Add"))
        self.remove_button.setText(_translate("shift", "Remove"))
        self.label.setText(_translate("shift", "Shift Name"))
        self.label_2.setText(_translate("shift", "Start"))
        self.label_3.setText(_translate("shift", "End"))
        self.label_4.setText(_translate("shift", "REWET only supports hours currently"))
        self.apply_button.setText(_translate("shift", "Apply"))
        self.cancel_button.setText(_translate("shift", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shift = QtWidgets.QDialog()
    ui = Ui_shift()
    ui.setupUi(shift)
    shift.show()
    sys.exit(app.exec_())

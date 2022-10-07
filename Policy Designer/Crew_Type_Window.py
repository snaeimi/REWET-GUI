# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crew_type.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_crew_type_window(object):
    def setupUi(self, crew_type_window):
        crew_type_window.setObjectName("crew_type_window")
        crew_type_window.setWindowModality(QtCore.Qt.ApplicationModal)
        crew_type_window.resize(425, 305)
        self.crew_type_list = QtWidgets.QListWidget(crew_type_window)
        self.crew_type_list.setGeometry(QtCore.QRect(20, 100, 281, 192))
        self.crew_type_list.setObjectName("crew_type_list")
        self.crew_type_input = QtWidgets.QLineEdit(crew_type_window)
        self.crew_type_input.setGeometry(QtCore.QRect(20, 60, 281, 27))
        self.crew_type_input.setObjectName("crew_type_input")
        self.apply_button = QtWidgets.QPushButton(crew_type_window)
        self.apply_button.setGeometry(QtCore.QRect(310, 140, 92, 29))
        self.apply_button.setObjectName("apply_button")
        self.remove_button = QtWidgets.QPushButton(crew_type_window)
        self.remove_button.setGeometry(QtCore.QRect(310, 100, 92, 29))
        self.remove_button.setObjectName("remove_button")
        self.add_button = QtWidgets.QPushButton(crew_type_window)
        self.add_button.setGeometry(QtCore.QRect(310, 60, 92, 29))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(crew_type_window)
        self.cancel_button.setGeometry(QtCore.QRect(310, 180, 92, 29))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(crew_type_window)
        QtCore.QMetaObject.connectSlotsByName(crew_type_window)

    def retranslateUi(self, crew_type_window):
        _translate = QtCore.QCoreApplication.translate
        crew_type_window.setWindowTitle(_translate("crew_type_window", "Dialog"))
        self.apply_button.setText(_translate("crew_type_window", "Apply"))
        self.remove_button.setText(_translate("crew_type_window", "Remove"))
        self.add_button.setText(_translate("crew_type_window", "Add"))
        self.cancel_button.setText(_translate("crew_type_window", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    crew_type_window = QtWidgets.QDialog()
    ui = Ui_crew_type_window()
    ui.setupUi(crew_type_window)
    crew_type_window.show()
    sys.exit(app.exec_())

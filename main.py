#! /usr/bin/env python
# author : Htmldigger
# Date : 4thfeb2022
# ## #####################################################
# Import Module here.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt

import os, sys
import datetime

class Ui_Form(object):
    def set_time(self):
        date1 = QDateTime.currentDateTime()
        date_string = date1.toString()
        self.date_print.setText(date_string)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(442, 319)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Special__Name = QtWidgets.QHBoxLayout()
        self.Special__Name.setObjectName("Special__Name")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.Special__Name.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setObjectName("lineEdit")
        self.Special__Name.addWidget(self.lineEdit)
        self.checkBox_special_name = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_special_name.setObjectName("checkBox_special_name")
        self.Special__Name.addWidget(self.checkBox_special_name)
        self.gridLayout_4.addLayout(self.Special__Name, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.final_Name_print = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.final_Name_print.setFont(font)
        self.final_Name_print.setAlignment(QtCore.Qt.AlignCenter)
        self.final_Name_print.setWordWrap(True)
        self.final_Name_print.setObjectName("final_Name_print")
        self.verticalLayout_3.addWidget(self.final_Name_print)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel = QtWidgets.QPushButton(self.frame_2)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.ok = QtWidgets.QPushButton(self.frame_2)
        self.ok.setObjectName("ok")

        self.ok.released.connect(self.press_button)

        self.horizontalLayout.addWidget(self.ok)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Main_Lable = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.Main_Lable.setFont(font)
        self.Main_Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_Lable.setObjectName("Main_Lable")
        self.verticalLayout.addWidget(self.Main_Lable)
        self.date_print = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.date_print.setFont(font)
        self.date_print.setAlignment(QtCore.Qt.AlignCenter)
        self.date_print.setObjectName("date_print")
        self.verticalLayout.addWidget(self.date_print)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(Form)
        self.cancel.released.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit, self.checkBox_special_name)
        Form.setTabOrder(self.checkBox_special_name, self.ok)
        Form.setTabOrder(self.ok, self.cancel)

# ## #################################################################################
# ## Local Time start. 
# ## #################################################################################
        timer = QtCore.QTimer(Form)
        timer.timeout.connect(self.set_time)
        timer.start(1000)    

# ## #################################################################################
# ## Button pressed print data and make directory.
# ## #################################################################################

    def press_button(self):
        data = self.lineEdit.text()
        print(data)
        today = datetime.datetime.now()
        if self.checkBox_special_name.isChecked():
            self.final_Name_print.setText(today.strftime(f"%B_%d-%m-%Y_{data}_%H-%M-%S"))
            try:
                os.makedirs(today.strftime(f"%B_%d-%m-%Y_{data}_%H-%M-%S"))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        else:
            self.final_Name_print.setText(today.strftime("%B_%d-%m-%Y_%H-%M-%S"))
            try:
                os.makedirs(today.strftime("%B_%d-%m-%Y_%H-%M-%S"))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FolderCreation"))
        self.label.setText(_translate("Form", "Special name : "))
        self.checkBox_special_name.setText(_translate("Form", "enable"))
        self.final_Name_print.setText(_translate("Form", "TextLabel"))
        self.cancel.setText(_translate("Form", "Cancel"))
        self.ok.setText(_translate("Form", "OK"))
        self.Main_Lable.setText(_translate("Form", "<p><span style=\" font-weight:600; color:#3f6a00;\">Folder</span><span style=\" color:#445680;\">Creation</span><span style=\" color:#445680; vertical-align:super;\">v01</span></p>"))
        self.date_print.setText(_translate("Form", "feb_02_2022"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

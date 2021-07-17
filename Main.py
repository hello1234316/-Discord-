# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '123.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

from pypresence import Presence, Activity
import time
import os
import sys
import subprocess
class Ui_Dialog(object):

    bool = False
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 535)
        self.const_ID = QtWidgets.QLabel(Dialog)
        self.const_ID.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.const_ID.setObjectName("const_ID")
        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setGeometry(QtCore.QRect(10, 50, 251, 20))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.const_Details = QtWidgets.QLabel(Dialog)
        self.const_Details.setGeometry(QtCore.QRect(10, 140, 101, 20))
        self.const_Details.setObjectName("const_Details")
        self.lineEdit_Details = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Details.setGeometry(QtCore.QRect(10, 160, 251, 20))
        self.lineEdit_Details.setObjectName("lineEdit_Details")
        self.lineEdit_State = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_State.setGeometry(QtCore.QRect(10, 230, 251, 20))
        self.lineEdit_State.setObjectName("lineEdit_State")
        self.lineEdit_Image = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Image.setGeometry(QtCore.QRect(10, 300, 251, 20))
        self.lineEdit_Image.setObjectName("lineEdit_Image")
        self.const_State = QtWidgets.QLabel(Dialog)
        self.const_State.setGeometry(QtCore.QRect(10, 210, 47, 21))
        self.const_State.setObjectName("const_State")
        self.const_Image = QtWidgets.QLabel(Dialog)
        self.const_Image.setGeometry(QtCore.QRect(10, 280, 61, 21))
        self.const_Image.setObjectName("const_Image")
        self.Client_ID = QtWidgets.QLabel(Dialog)
        self.Client_ID.setGeometry(QtCore.QRect(90, 30, 171, 16))
        self.Client_ID.setObjectName("Client_ID")
        self.Details = QtWidgets.QLabel(Dialog)
        self.Details.setGeometry(QtCore.QRect(70, 140, 191, 20))
        self.Details.setObjectName("Details")
        self.State = QtWidgets.QLabel(Dialog)
        self.State.setGeometry(QtCore.QRect(60, 210, 201, 21))
        self.State.setObjectName("State")
        self.Image = QtWidgets.QLabel(Dialog)
        self.Image.setGeometry(QtCore.QRect(70, 280, 191, 21))
        self.Image.setObjectName("Image")
        self.saveChange = QtWidgets.QPushButton(Dialog)
        self.saveChange.setGeometry(QtCore.QRect(10, 360, 251, 31))
        self.saveChange.setObjectName("saveChange")
        self.checkBox_Details = QtWidgets.QCheckBox(Dialog)
        self.checkBox_Details.setGeometry(QtCore.QRect(280, 160, 16, 16))
        self.checkBox_Details.setText("")
        self.checkBox_Details.setObjectName("checkBox_Details")
        self.checkBox_State = QtWidgets.QCheckBox(Dialog)
        self.checkBox_State.setGeometry(QtCore.QRect(280, 230, 16, 16))
        self.checkBox_State.setText("")
        self.checkBox_State.setObjectName("checkBox_State")
        self.checkBox_Image = QtWidgets.QCheckBox(Dialog)
        self.checkBox_Image.setGeometry(QtCore.QRect(280, 300, 16, 16))
        self.checkBox_Image.setText("")
        self.checkBox_Image.setObjectName("checkBox_Image")
        self.showDetails = QtWidgets.QLabel(Dialog)
        self.showDetails.setGeometry(QtCore.QRect(300, 160, 91, 16))
        self.showDetails.setObjectName("showDetails")
        self.showState = QtWidgets.QLabel(Dialog)
        self.showState.setGeometry(QtCore.QRect(300, 230, 91, 16))
        self.showState.setObjectName("showState")
        self.showImage = QtWidgets.QLabel(Dialog)
        self.showImage.setGeometry(QtCore.QRect(300, 300, 91, 16))
        self.showImage.setObjectName("showImage")
        self.showTimer = QtWidgets.QLabel(Dialog)
        self.showTimer.setGeometry(QtCore.QRect(300, 370, 91, 16))
        self.showTimer.setObjectName("showTimer")
        self.checkBox_Timer = QtWidgets.QCheckBox(Dialog)
        self.checkBox_Timer.setGeometry(QtCore.QRect(280, 370, 16, 16))
        self.checkBox_Timer.setText("")
        self.checkBox_Timer.setObjectName("checkBox_Timer")
        self.Start = QtWidgets.QPushButton(Dialog)
        self.Start.setGeometry(QtCore.QRect(10, 420, 81, 31))
        self.Start.setObjectName("Start")
        self.Stop = QtWidgets.QPushButton(Dialog)
        self.Stop.setGeometry(QtCore.QRect(100, 420, 81, 31))
        self.Stop.setObjectName("Stop")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Buttons
        self.saveChange.clicked.connect(self.f_save)
        self.Start.clicked.connect(self.f_start)
        self.Stop.clicked.connect(self.f_stop)
    def retranslateUi(self, Dialog):

        # Read the arguments
        with open(os.getcwd() + '/run/dist/tmp.txt' , 'r') as f:
            self._Client_ID = f.readline().strip()
            self._Details = f.readline().strip()
            self._State = f.readline().strip()
            self._Image = f.readline().strip()

            self.tmp_Client_ID = self._Client_ID
            self.tmp_Details = self._Details
            self.tmp_State = self._State
            self.tmp_Image = self._Image

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "rich-presence"))
        self.const_ID.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Client ID : </span></p></body></html>"))
        self.const_Details.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Details :</span></p></body></html>"))
        self.const_State.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">State :</span></p></body></html>"))
        self.const_Image.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Image :</span></p></body></html>"))
        self.Client_ID.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">{_Client_ID}</span></p></body></html>").format(_Client_ID = self._Client_ID))
        self.Details.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">{_Details}</span></p></body></html>").format(_Details = self._Details))
        self.State.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">{_State}</span></p></body></html>").format(_State = self._State))
        self.Image.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">{_Image}</span></p></body></html>").format(_Image = self._Image))
        self.saveChange.setText(_translate("Dialog", "Save change"))
        self.showDetails.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Show details</span></p></body></html>"))
        self.showState.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Show state</span></p></body></html>"))
        self.showImage.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Show image</span></p></body></html>"))
        self.showTimer.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Show timer</span></p></body></html>"))
        self.Start.setText(_translate("Dialog", "Start"))
        self.Stop.setText(_translate("Dialog", "Stop"))

    # Function definition

    def f_save(self):

        # Set the arguments
        self.tmp_Client_ID = self.lineEdit_ID.text()
        self.tmp_Details = self.lineEdit_Details.text()
        self.tmp_State = self.lineEdit_State.text()
        self.tmp_Image = self.lineEdit_Image.text()

        # Save the arguments
        with open(os.getcwd() + '/run/dist/arguments.txt' , 'w+') as f:
            if self.tmp_Client_ID == "":
                f.write(self._Client_ID + '\n')
            else:
                f.write(self.tmp_Client_ID + '\n')

            if self.tmp_Details == "":
                f.write(self._Details + '\n')
            else:
                f.write(self.tmp_Details + '\n')

            if self.tmp_State == "":
                f.write(self._State + '\n')
            else:
                f.write(self.tmp_State + '\n')

            if self.tmp_Image == "":
                f.write(self._Image + '\n')
            else:
                f.write(self.tmp_Image + '\n')

        with open(os.getcwd() + '/run/dist/tmp.txt' , 'w+') as f:
            if self.tmp_Client_ID == "":
                f.write(self._Client_ID + '\n')
            else:
                f.write(self.tmp_Client_ID + '\n')

            if self.tmp_Details == "":
                f.write(self._Details + '\n')
            else:
                f.write(self.tmp_Details + '\n')

            if self.tmp_State == "":
                f.write(self._State + '\n')
            else:
                f.write(self.tmp_State + '\n')

            if self.tmp_Image == "":
                f.write(self._Image + '\n')
            else:
                f.write(self.tmp_Image + '\n')

        with open(os.getcwd() + '/run/dist/arguments.txt' , 'r') as f:
            self._Client_ID = f.readline().strip()
            self._Details = f.readline().strip()
            self._State = f.readline().strip()
            self._Image = f.readline().strip()

        if len(self.tmp_Client_ID) + len(self.tmp_Details) + len(self.tmp_State) + len(self.tmp_Image) > 0:
            print('成功保存設定 !')

        # Update the arguments
        _translate = QtCore.QCoreApplication.translate
        self.Client_ID.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">{_Client_ID}</span></p></body></html>").format(_Client_ID = self._Client_ID))
        self.Details.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">{_Details}</span></p></body></html>").format(_Details = self._Details))
        self.State.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">{_State}</span></p></body></html>").format(_State = self._State))
        self.Image.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">{_Image}</span></p></body></html>").format(_Image = self._Image))

    def f_start(self):
        try:
            self.bool = subprocess.call('tasklist |find /i"rich-presence.exe"' , shell = True)
        except Exception as e:
            raise

        if self.checkBox_State.isChecked() == True:
            if len(self.tmp_State) >= 2:
                self.s = True
            else:
                self.s = False
        else:
            self.s = True
            
        if self.s == False:
            print('State 狀態至少要有兩個字元 !')
        elif self.bool == 1 and self.s == True:
            self.check()

            with open(os.getcwd() + '/run/dist/arguments.txt' , 'r') as f:
                self._1 = f.readline().strip()
                self._2 = f.readline().strip()
                self._3 = f.readline().strip()
                self._4 = f.readline().strip()
                self._5 = f.readline().strip()
            os.system('start {exe} {_1} {_2} {_3} {_4} {_5}'.format(exe = os.getcwd() + '/run/dist/rich-presence.exe' , _1 = self._1 , _2 = self._2 , _3 = self._3 , _4 = self._4 , _5 = self._5))
            print('Discord 自定義狀態保持中 ...')
        else:
            print('你已經執行過了')

    def f_stop(self):
        try:
            self.bool = subprocess.call('tasklist |find /i"rich-presence.exe"' , shell = True)
        except Exception as e:
            raise
        if self.bool == 0:
            self.bool = subprocess.call('taskkill /f /im "rich-presence.exe"' , shell = True)
            print('Discord 自定義狀態結束')
        else:
            print('程式已經是停止狀態')
    def check(self):
        with open(os.getcwd() + '/run/dist/arguments.txt' , 'w+') as f:
            f.write(self._Client_ID + '\n')

            if self.checkBox_Details.isChecked():
                f.write(self._Details + '\n')
            else:
                f.write('None' + '\n')
            if self.checkBox_State.isChecked():
                f.write(self._State + '\n')
            else:
                f.write('None' + '\n')
            if self.checkBox_Image.isChecked():
                f.write(self._Image + '\n')
            else:
                f.write('None' + '\n')
            if self.checkBox_Timer.isChecked():
                f.write('True' + '\n')
            else:
                f.write('None' + '\n')

if __name__ == "__main__":
    # import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

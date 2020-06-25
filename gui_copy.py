# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import my_thread
from pathlib import Path


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, df):
        super().__init__()
        self.df = df
        self.video_path = ""

        self.resize(1203, 783)
        self.show_frame = QtWidgets.QLabel(self)
        self.show_frame.setGeometry(QtCore.QRect(60, 110, 640, 480))
        self.show_frame.setText("")
        self.show_frame.setObjectName("show_frame")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(60, 20, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showDialog)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


        # self.frame_value.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Object Counting"))
        self.pushButton.setText(_translate("Dialog", "Select Vİdeo"))
    
    @my_thread.pyqtSlot(my_thread.QImage)
    def setImage(self, image):
        self.show_frame.setPixmap(my_thread.QPixmap.fromImage(image))

    def showDialog(self):

        home_dir = str(Path.home())
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        self.video_path = fname[0]

        th = my_thread.Thread(self, self.video_path, self.df)
        th.changePixmap.connect(self.setImage)
        th.start()
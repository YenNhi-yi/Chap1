# Form implementation generated from reading ui file 'D:\PycharmProject\ProgrammingTechniques\Chapter_1\Ex24\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(696, 446)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 50, 441, 271))
        self.groupBox.setObjectName("groupBox")
        self.label_1 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(70, 30, 55, 61))
        self.label_1.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 55, 61))
        self.label_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(320, 30, 55, 61))
        self.label_3.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 151, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 151, 31))
        self.label_5.setObjectName("label_5")
        self.Machine = QtWidgets.QLabel(parent=self.groupBox)
        self.Machine.setGeometry(QtCore.QRect(200, 110, 141, 31))
        self.Machine.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Machine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Machine.setObjectName("Machine")
        self.Machine_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.Machine_2.setGeometry(QtCore.QRect(200, 160, 141, 31))
        self.Machine_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Machine_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Machine_2.setObjectName("Machine_2")
        self.pushButtonR = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonR.setGeometry(QtCore.QRect(20, 220, 121, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\PycharmProject\\ProgrammingTechniques\\Chapter_1\\Ex24\\ui\\../images/random.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonR.setIcon(icon)
        self.pushButtonR.setObjectName("pushButtonR")
        self.pushButtonN = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonN.setGeometry(QtCore.QRect(160, 220, 121, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\PycharmProject\\ProgrammingTechniques\\Chapter_1\\Ex24\\ui\\../images/new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonN.setIcon(icon1)
        self.pushButtonN.setObjectName("pushButtonN")
        self.pushButtonE = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonE.setGeometry(QtCore.QRect(300, 220, 121, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\PycharmProject\\ProgrammingTechniques\\Chapter_1\\Ex24\\ui\\../images/Exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonE.setIcon(icon2)
        self.pushButtonE.setObjectName("pushButtonE")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nguyễn Thị Yến Nhi"))
        self.groupBox.setTitle(_translate("MainWindow", "Lucky Game"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Machine money:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Player money:</span></p></body></html>"))
        self.Machine.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Machine_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButtonR.setText(_translate("MainWindow", "Random"))
        self.pushButtonN.setText(_translate("MainWindow", "New game"))
        self.pushButtonE.setText(_translate("MainWindow", "Exit"))

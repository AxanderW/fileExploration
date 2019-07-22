# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specialprojects_secwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_SpecialProjectsSecWindow(QObject):
    def setupUi(self, SpecialProjectsSecWindow):
        SpecialProjectsSecWindow.setObjectName("SpecialProjectsSecWindow")
        SpecialProjectsSecWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SpecialProjectsSecWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 70, 701, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 681, 251))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        # New button to execute process
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 2, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.debugTextBrowser.setGeometry(QtCore.QRect(60, 380, 681, 131))
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        SpecialProjectsSecWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpecialProjectsSecWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SpecialProjectsSecWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpecialProjectsSecWindow)
        self.statusbar.setObjectName("statusbar")
        SpecialProjectsSecWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SpecialProjectsSecWindow)
        self.pushButton.clicked.connect(self.browseDirSlot)
        self.pushButton_2.clicked.connect(self.browseTargetSlot)
        self.pushButton_3.clicked.connect(self.browseFileSlot)
        self.lineEdit.returnPressed.connect(self.releasePresedSlot)
        self.lineEdit_2.returnPressed.connect(self.releasePresedSlot)
        self.lineEdit_3.returnPressed.connect(self.releasePresedSlot)
        self.lineEdit_4.returnPressed.connect(self.releasePresedSlot)
        # New execute button
        self.pushButton_4.clicked.connect(self.executeSlot)

        QtCore.QMetaObject.connectSlotsByName(SpecialProjectsSecWindow)

    def retranslateUi(self, SpecialProjectsSecWindow):
        _translate = QtCore.QCoreApplication.translate
        SpecialProjectsSecWindow.setWindowTitle(_translate("SpecialProjectsSecWindow", "MainWindow"))
        self.label_4.setText(_translate("SpecialProjectsSecWindow", "Fleet Study Automation Tool"))
        self.label.setText(_translate("SpecialProjectsSecWindow", "Special Projects"))
        self.label_2.setText(_translate("SpecialProjectsSecWindow", "Root Directory/Folder"))
        self.pushButton.setText(_translate("SpecialProjectsSecWindow", "Browse"))
        self.label_3.setText(_translate("SpecialProjectsSecWindow", "Target Directory/Folder"))
        self.pushButton_2.setText(_translate("SpecialProjectsSecWindow", "Browse"))
        self.label_5.setText(_translate("SpecialProjectsSecWindow", "File Name"))
        self.pushButton_3.setText(_translate("SpecialProjectsSecWindow", "Browse"))
        self.label_6.setText(_translate("SpecialProjectsSecWindow", "Search File:"))

        # New execute button
        self.pushButton_4.setText(_translate("SpecialProjectsSecWindow", "Execute"))



    @pyqtSlot( )
    def browseDirSlot(self):
        pass

    @pyqtSlot( )
    def browseFileSlot(self):
        pass


    @pyqtSlot( )
    def releasePresedSlot(self):
        pass

    @pyqtSlot( )
    def browseTargetSlot(self):
        pass

    @pyqtSlot( )
    def executeSlot(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpecialProjectsSecWindow = QtWidgets.QMainWindow()
    ui = Ui_SpecialProjectsSecWindow()
    ui.setupUi(SpecialProjectsSecWindow)
    SpecialProjectsSecWindow.show()
    sys.exit(app.exec_())


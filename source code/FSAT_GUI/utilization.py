# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'utilization.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_UtilizationMainWindow(QObject):
    def setupUi(self, UtilizationMainWindow):
        UtilizationMainWindow.setObjectName("UtilizationMainWindow")
        UtilizationMainWindow.resize(1216, 767)
        self.centralwidget = QtWidgets.QWidget(UtilizationMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 117, 42))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.debugTextBrowser.setGeometry(QtCore.QRect(20, 480, 681, 151))
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(29)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 60, 491, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 3)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(650, 90, 481, 311))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1010, 410, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        UtilizationMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UtilizationMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1216, 26))
        self.menubar.setObjectName("menubar")
        UtilizationMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UtilizationMainWindow)
        self.statusbar.setObjectName("statusbar")
        UtilizationMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UtilizationMainWindow)
        self.pushButton.clicked.connect(self.browseSlot)
        self.pushButton_3.clicked.connect(self.showTableSlot)
        self.pushButton_2.clicked.connect(self.clearTableSlot)
        self.pushButton_4.clicked.connect(self.secondUtilWindowSlot)
        self.lineEdit.returnPressed.connect(self.returnPressedSlot)
        self.pushButton_5.clicked.connect(self.writeDocSlot)
        QtCore.QMetaObject.connectSlotsByName(UtilizationMainWindow)

    def retranslateUi(self, UtilizationMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UtilizationMainWindow.setWindowTitle(_translate("UtilizationMainWindow", "MainWindow"))
        self.label.setText(_translate("UtilizationMainWindow", "Fleet Study Automation Tool"))
        self.label_3.setText(_translate("UtilizationMainWindow", "Utilization"))
        self.label_2.setText(_translate("UtilizationMainWindow", "File Name"))
        self.pushButton.setText(_translate("UtilizationMainWindow", "Browse"))
        self.pushButton_3.setText(_translate("UtilizationMainWindow", "Show"))
        self.pushButton_2.setText(_translate("UtilizationMainWindow", "Clear"))
        self.pushButton_4.setText(_translate("UtilizationMainWindow", "Next"))
        self.pushButton_5.setText(_translate("UtilizationMainWindow", "Write Doc"))



    @pyqtSlot( )
    def browseSlot(self):
        pass

    @pyqtSlot( )
    def showTableSlot(self):
        pass
    @pyqtSlot( )
    def clearTableSlot(self):
        pass
    @pyqtSlot( )
    def secondUtilWindowSlot(self):
        pass
    @pyqtSlot( )
    def returnPressedSlot(self):
        pass
    @pyqtSlot( )
    def writeDocSlot(self):
        pass
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UtilizationMainWindow = QtWidgets.QMainWindow()
    ui = Ui_UtilizationMainWindow()
    ui.setupUi(UtilizationMainWindow)
    UtilizationMainWindow.show()
    sys.exit(app.exec_())


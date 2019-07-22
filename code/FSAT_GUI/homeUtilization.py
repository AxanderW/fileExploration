# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeUtilization.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_DataViewMainWindow(QObject):
    def setupUi(self, DataViewMainWindow):
        DataViewMainWindow.setObjectName("DataViewMainWindow")
        DataViewMainWindow.resize(1285, 802)
        self.centralwidget = QtWidgets.QWidget(DataViewMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(29)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 117, 42))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.debugtextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.debugtextBrowser.setGeometry(QtCore.QRect(360, 610, 551, 121))
        self.debugtextBrowser.setObjectName("debugtextBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 80, 1251, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 450, 601, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.backButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_4.addWidget(self.backButton)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.backButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.backButton_2.setFont(font)
        self.backButton_2.setObjectName("backButton_2")
        self.horizontalLayout_4.addWidget(self.backButton_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 611, 411))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout.addWidget(self.browseButton, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.sheetNamelineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.sheetNamelineEdit.setText("")
        self.sheetNamelineEdit.setObjectName("sheetNamelineEdit")
        self.gridLayout.addWidget(self.sheetNamelineEdit, 1, 1, 1, 1)
        self.tableView_2 = QtWidgets.QTableView(self.layoutWidget2)
        self.tableView_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView_2.setAlternatingRowColors(True)
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView_2.horizontalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.tableView_2, 2, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(630, 0, 621, 519))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 450, 621, 32))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.backButton_4 = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.backButton_4.setFont(font)
        self.backButton_4.setObjectName("backButton_4")
        self.horizontalLayout.addWidget(self.backButton_4)
        self.backButton_3 = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.backButton_3.setFont(font)
        self.backButton_3.setObjectName("backButton_3")
        self.horizontalLayout.addWidget(self.backButton_3)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(110, 0, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableView_3 = QtWidgets.QTableView(self.frame_2)
        self.tableView_3.setGeometry(QtCore.QRect(0, 67, 611, 341))
        self.tableView_3.setAlternatingRowColors(True)
        self.tableView_3.setObjectName("tableView_3")
        self.horizontalLayout_3.addWidget(self.frame)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        DataViewMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataViewMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 26))
        self.menubar.setObjectName("menubar")
        DataViewMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataViewMainWindow)
        self.statusbar.setObjectName("statusbar")
        DataViewMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DataViewMainWindow)
        self.backButton_2.clicked.connect(self.clearCustDataSlot)
        self.pushButton_9.clicked.connect(self.loadDataFullSlot)
        self.pushButton_8.clicked.connect(self.loadDataPrevSlot)
        self.backButton.clicked.connect(self.backSlot)
        self.backButton_3.clicked.connect(self.clearInvenDataSlot)
        self.backButton_4.clicked.connect(self.cleanDataSlot)
        self.pushButton_10.clicked.connect(self.loadInvenDataFullSlot)
        self.pushButton_11.clicked.connect(self.loadInvenDataPrevSlot)
        self.browseButton.clicked.connect(self.browseSlot)
        QtCore.QMetaObject.connectSlotsByName(DataViewMainWindow)

    def retranslateUi(self, DataViewMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DataViewMainWindow.setWindowTitle(_translate("DataViewMainWindow", "MainWindow"))
        self.label_3.setText(_translate("DataViewMainWindow", "Utilization"))
        self.label.setText(_translate("DataViewMainWindow", "Fleet Study Automation Tool"))
        self.backButton.setText(_translate("DataViewMainWindow", "Back"))
        self.pushButton_8.setText(_translate("DataViewMainWindow", "Load Data Preview"))
        self.pushButton_9.setText(_translate("DataViewMainWindow", "Load Data Full"))
        self.backButton_2.setText(_translate("DataViewMainWindow", "Clear"))
        self.label_5.setText(_translate("DataViewMainWindow", "File Name"))
        self.browseButton.setText(_translate("DataViewMainWindow", "Browse"))
        self.label_6.setText(_translate("DataViewMainWindow", "Sheet Name"))
        self.pushButton_11.setText(_translate("DataViewMainWindow", "Load Data Preview"))
        self.pushButton_10.setText(_translate("DataViewMainWindow", "Load Data Full"))
        self.backButton_4.setText(_translate("DataViewMainWindow", "Scrub Data"))
        self.backButton_3.setText(_translate("DataViewMainWindow", "Clear"))
        self.label_2.setText(_translate("DataViewMainWindow", "Fleet Inventory Template"))

    @pyqtSlot( )
    def returnPressedSlot(self):
        pass


    @pyqtSlot( )
    def clearCustDataSlot(self):
        pass


    @pyqtSlot( )
    def loadDataPrevSlot(self):
        pass


    @pyqtSlot( )
    def loadDataFullSlot(self):
        pass


    @pyqtSlot( )
    def backSlot(self):
        pass


    @pyqtSlot( )
    def browseSlot(self):
        pass



    @pyqtSlot( )
    def downloadDataSlot (self):
        pass

    @pyqtSlot( )
    def cleanDataSlot(self):
        pass

    @pyqtSlot( )
    def clearInvenDataSlot(self):
        pass

    @pyqtSlot( )
    def loadInvenDataPrevSlot(self):
        pass

    @pyqtSlot( )

    def loadInvenDataFullSlot(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataViewMainWindow = QtWidgets.QMainWindow()
    ui = Ui_DataViewMainWindow()
    ui.setupUi(DataViewMainWindow)
    DataViewMainWindow.show()
    sys.exit(app.exec_())


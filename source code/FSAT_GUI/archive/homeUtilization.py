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
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 601, 421))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView_2 = QtWidgets.QTableView(self.layoutWidget1)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout_2.addWidget(self.tableView_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 450, 601, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.backButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_4.addWidget(self.backButton)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.backButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.backButton_2.setFont(font)
        self.backButton_2.setObjectName("backButton_2")
        self.horizontalLayout_4.addWidget(self.backButton_2)
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 621, 431))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.tableView_3 = QtWidgets.QTableView(self.layoutWidget2)
        self.tableView_3.setObjectName("tableView_3")
        self.gridLayout_3.addWidget(self.tableView_3, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(0, 450, 621, 32))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.backButton_4 = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.backButton_4.setFont(font)
        self.backButton_4.setObjectName("backButton_4")
        self.horizontalLayout.addWidget(self.backButton_4)
        self.backButton_3 = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.backButton_3.setFont(font)
        self.backButton_3.setObjectName("backButton_3")
        self.horizontalLayout.addWidget(self.backButton_3)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        DataViewMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataViewMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 26))
        self.menubar.setObjectName("menubar")
        DataViewMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataViewMainWindow)
        self.statusbar.setObjectName("statusbar")
        DataViewMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DataViewMainWindow)
        self.lineEdit_2.returnPressed.connect(self.returnPressedSlot)
        self.browseButton.clicked.connect(self.browseSlot)
        self.backButton_2.clicked.connect(self.clearCustDataSlot)
        self.pushButton_9.clicked.connect(self.loadDataFullSlot)
        self.pushButton_8.clicked.connect(self.loadDataPrevSlot)
        self.backButton.clicked.connect(self.backSlot)
        self.backButton_3.clicked.connect(self.clearInvenDataSlot)
        self.backButton_4.clicked.connect(self.cleanDataSlot)
        self.pushButton_10.clicked.connect(self.loadInvenDataFullSlot)
        self.pushButton_11.clicked.connect(self.loadInvenDataPrevSlot)
        QtCore.QMetaObject.connectSlotsByName(DataViewMainWindow)

    def retranslateUi(self, DataViewMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DataViewMainWindow.setWindowTitle(_translate("DataViewMainWindow", "MainWindow"))
        self.label_3.setText(_translate("DataViewMainWindow", "Utilization"))
        self.label.setText(_translate("DataViewMainWindow", "Fleet Study Automation Tool"))
        self.label_5.setText(_translate("DataViewMainWindow", "File Name"))
        self.browseButton.setText(_translate("DataViewMainWindow", "Browse"))
        self.backButton.setText(_translate("DataViewMainWindow", "Back"))
        self.pushButton_8.setText(_translate("DataViewMainWindow", "Load Data Preview"))
        self.pushButton_9.setText(_translate("DataViewMainWindow", "Load Data Full"))
        self.backButton_2.setText(_translate("DataViewMainWindow", "Clear"))
        self.label_2.setText(_translate("DataViewMainWindow", "Fleet Inventory Template"))
        self.pushButton_11.setText(_translate("DataViewMainWindow", "Load Data Preview"))
        self.pushButton_10.setText(_translate("DataViewMainWindow", "Load Data Full"))
        self.backButton_4.setText(_translate("DataViewMainWindow", "Scrub Data"))
        self.backButton_3.setText(_translate("DataViewMainWindow", "Clear"))

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


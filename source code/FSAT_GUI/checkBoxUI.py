# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkBoxUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QComboBox
from model import Model


class Ui_CheckboxMainWindow(QObject):
    def setupUi(self, CheckboxMainWindow):
        self.model = Model()

        CheckboxMainWindow.setObjectName("CheckboxMainWindow")
        CheckboxMainWindow.resize(944, 846)
        self.centralwidget = QtWidgets.QWidget(CheckboxMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.debugTextBrowser.setGeometry(QtCore.QRect(10, 740, 711, 51))
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 220, 481, 500))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # Add checkBoxes
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.widget1 = QtWidgets.QWidget(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")

        '''
        self.listCheckBox = ["CheckBox_1","CheckBox_2","CheckBox_1","CheckBox_5","CheckBox_6",
                            "CheckBox_7","CheckBox_8","CheckBox_9","CheckBox_10"]

        for i,v in enumerate(self.listCheckBox):
            self.listCheckBox[i] = QtWidgets.QCheckBox(v)
            self.gridLayout.addWidget(self.listCheckBox[i],i,5,1,1)


        
    
        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 5, 1, 1)

        '''







        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 173, 251, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 1, 471, 141))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.browseButton_3 = QtWidgets.QPushButton(self.widget)
        self.browseButton_3.setObjectName("browseButton_3")
        self.gridLayout_3.addWidget(self.browseButton_3, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.sheetNamelineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.sheetNamelineEdit_3.setText("")
        self.sheetNamelineEdit_3.setObjectName("sheetNamelineEdit_3")
        self.gridLayout_3.addWidget(self.sheetNamelineEdit_3, 1, 1, 1, 2)
        CheckboxMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CheckboxMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 26))
        self.menubar.setObjectName("menubar")
        CheckboxMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CheckboxMainWindow)
        self.statusbar.setObjectName("statusbar")
        CheckboxMainWindow.setStatusBar(self.statusbar)







        self.retranslateUi(CheckboxMainWindow)
        self.browseButton_3.clicked.connect(self.browseSlot)
        self.lineEdit_4.returnPressed.connect(self.browseReleasePressedSlot)
        self.sheetNamelineEdit_3.returnPressed.connect(self.sheetReleasePressedSlot)
        QtCore.QMetaObject.connectSlotsByName(CheckboxMainWindow)

    def retranslateUi(self, CheckboxMainWindow):
        _translate = QtCore.QCoreApplication.translate
        CheckboxMainWindow.setWindowTitle(_translate("CheckboxMainWindow", "MainWindow"))
        self.label.setText(_translate("CheckboxMainWindow", "Select Customer Fields Below:"))
        self.label_9.setText(_translate("CheckboxMainWindow", "File Name"))
        self.browseButton_3.setText(_translate("CheckboxMainWindow", "Browse"))
        self.label_10.setText(_translate("CheckboxMainWindow", "Sheet Name"))


    def debugPrint(self, msg):
        self.debugTextBrowser.append(msg)


    def refreshAll(self):
        self.lineEdit_4.setText(self.model.getFileName())


    @pyqtSlot( )
    def browseSlot(self):
        self.debugPrint("Browse key pressed")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "Excel Files (*.xlsx);; Excel Macro Enabled (*.xlsm)",
            options = options)

        if fileName:
            self.debugPrint("setting file name: " +fileName)
            self.model.setFileName(fileName)
            self.model.createDataFrame(fileName, self.sheetNamelineEdit_3.text())
            self.listCheckBox = self.model.getColumns(fileName, self.sheetNamelineEdit_3.text())

            self.listCheckBox_2 = ["CheckBox_1","CheckBox_2","CheckBox_1","CheckBox_5","CheckBox_6",
                            "CheckBox_7","CheckBox_8","CheckBox_9","CheckBox_10"]

            self.fleetDropDownList = self.model.getFleetColsUseable()
            self.cb = QComboBox()

            self.listlength = len(self.listCheckBox)

            for i,v in enumerate(self.listCheckBox):
                if i <=10:
                    
                    self.cb.addItems(self.fleetDropDownList)
                    self.gridLayout.addWidget(self.cb,i,1)
                    self.listCheckBox[i] = QtWidgets.QCheckBox(v)
                    self.gridLayout.addWidget(self.listCheckBox[i],i,0)
                    
                elif (i > 10 and i <20):
                    self.listCheckBox[i] = QtWidgets.QCheckBox(v)
                    self.gridLayout.addWidget(self.listCheckBox[i],i-11,3)

                elif (i>=20 and i < 30):
                    self.listCheckBox[i] = QtWidgets.QCheckBox(v)
                    self.gridLayout.addWidget(self.listCheckBox[i],i-21,6)


                elif(i>=30):
                    self.listCheckBox[i] = QtWidgets.QCheckBox(v)
                    self.gridLayout.addWidget(self.listCheckBox[i],i-31,9)                   


            self.refreshAll()        

    @pyqtSlot( )
    def browseReleasePressedSlot(self):
        self.debugPrint("Browse RETURN key pressed")

        fileName = self.lineEdit_4.text()
        if self.model.isValid(fileName):
            self.model.setFileName(self.lineEdit_4.text())
            self.model.createDataFrame(fileName, self.sheetNamelineEdit_3.text())
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name! \n" + fileName)
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                |QtWidgets.QMessageBox.Cancel)

            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit_4.setText(" ")
            self.refreshAll()
            self.debugPrint("Invalid file specified: "+fileName)

    @pyqtSlot( )
    def sheetReleasePressedSlot(self):
        self.debugPrint("Sheet RETURN key pressed")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckboxMainWindow = QtWidgets.QMainWindow()
    ui = Ui_CheckboxMainWindow()
    ui.setupUi(CheckboxMainWindow)
    CheckboxMainWindow.show()
    sys.exit(app.exec_())


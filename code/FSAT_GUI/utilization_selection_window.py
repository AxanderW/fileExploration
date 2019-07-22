# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'utilization_selection_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_UtilizationSelectionMainWindow(QObject):
    def setupUi(self, UtilizationSelectionMainWindow):
        UtilizationSelectionMainWindow.setObjectName("UtilizationSelectionMainWindow")
        UtilizationSelectionMainWindow.resize(800, 658)
        self.centralwidget = QtWidgets.QWidget(UtilizationSelectionMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 110, 661, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 621, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mapRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.mapRadioButton.setFont(font)
        self.mapRadioButton.setObjectName("mapRadioButton")
        self.verticalLayout.addWidget(self.mapRadioButton)
        self.scrubRadioButton_1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.scrubRadioButton_1.setFont(font)
        self.scrubRadioButton_1.setObjectName("scrubRadioButton_1")
        self.verticalLayout.addWidget(self.scrubRadioButton_1)
        self.scrubRadioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.scrubRadioButton_2.setFont(font)
        self.scrubRadioButton_2.setObjectName("scrubRadioButton_2")
        self.verticalLayout.addWidget(self.scrubRadioButton_2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 510, 461, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 440, 751, 36))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nextButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        UtilizationSelectionMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UtilizationSelectionMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        UtilizationSelectionMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UtilizationSelectionMainWindow)
        self.statusbar.setObjectName("statusbar")
        UtilizationSelectionMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UtilizationSelectionMainWindow)
        self.nextButton.clicked.connect(self.nextSlot)
        self.backButton.clicked.connect(self.backSlot)
        self.mapRadioButton.toggled['bool'].connect(self.onRadioSlot)
        self.scrubRadioButton_1.toggled['bool'].connect(self.onRadioSlot)
        self.scrubRadioButton_2.toggled['bool'].connect(self.onRadioSlot)
        self.radioButton_4.toggled['bool'].connect(self.onRadioSlot)
        QtCore.QMetaObject.connectSlotsByName(UtilizationSelectionMainWindow)

    def retranslateUi(self, UtilizationSelectionMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UtilizationSelectionMainWindow.setWindowTitle(_translate("UtilizationSelectionMainWindow", "MainWindow"))
        self.label_2.setText(_translate("UtilizationSelectionMainWindow", "Please select an option below:"))
        self.mapRadioButton.setText(_translate("UtilizationSelectionMainWindow", "Map Customer Data to Fleet Template"))
        self.scrubRadioButton_1.setText(_translate("UtilizationSelectionMainWindow", "Scrub Customer Data"))
        self.scrubRadioButton_2.setText(_translate("UtilizationSelectionMainWindow", "Scrub Fleet Upload Template"))
        self.radioButton_4.setText(_translate("UtilizationSelectionMainWindow", "Utilization Express"))
        self.label.setText(_translate("UtilizationSelectionMainWindow", "Utilization Main"))
        self.label_3.setText(_translate("UtilizationSelectionMainWindow", "TestLabel"))
        self.label_4.setText(_translate("UtilizationSelectionMainWindow", "Fleet Study Automation Tool"))
        self.backButton.setText(_translate("UtilizationSelectionMainWindow", "Back"))
        self.nextButton.setText(_translate("UtilizationSelectionMainWindow", "Next"))


    @pyqtSlot( )
    def nextSlot(self):
        pass

    @pyqtSlot( )
    def backSlot(self):
        pass

    @pyqtSlot( )
    def onRadioSlot(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UtilizationSelectionMainWindow = QtWidgets.QMainWindow()
    ui = Ui_UtilizationSelectionMainWindow()
    ui.setupUi(UtilizationSelectionMainWindow)
    UtilizationSelectionMainWindow.show()
    sys.exit(app.exec_())


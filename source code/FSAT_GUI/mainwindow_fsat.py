from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QPushButton, QMainWindow, QGroupBox, QRadioButton, QHBoxLayout
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, pyqtSlot, QObject
# will create a new window to start utilization study
# will create a new window to start utilization study
from homeUtilizationApp import HomeUtilizationUIClass
from specialprojectsApp import SpecialProjectsClass

class MainWindow(QDialog):
    def __init__ (self):
        super().__init__()


        self.title = "Fleet Study Automation Tool Home"
        self.left = 300
        self.top = 400
        self.width = 1000
        self.height = 350
        self.iconName = "images/corcentric_logo.jpg"

        # call init function
        self.InitWindow()

    
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))

        self.setGeometry(self.left, self.top, self.width,self.height)

        self.radioButton()

        vbox= QVBoxLayout()
        vbox.addWidget(self.groupBox)

        # add start button
        self.button1 = QPushButton("Start Study")
        self.button1.setFont(QtGui.QFont("Calibri", 12))
        self.button1.clicked.connect(self.onStartStudy)

        vbox.addWidget(self.button1)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Calibri",12))
        vbox.addWidget(self.label)

        # add layout
        self.setLayout(vbox)
        self.show()

    def radioButton(self):
        self.groupBox = QGroupBox("Select a Fleet Study Category")
        self.groupBox.setFont(QtGui.QFont("Calibri",16))

        hboxLayout = QHBoxLayout()

        # Create radio buttons
        # Create Utilization button
        self.radiobtn1 = QRadioButton("Utilization")
        # makes radio option the default checked
        # self.radiobtn1.setChecked(True)
        self.radiobtn1.setIcon(QtGui.QIcon("images/utilization_icon.png"))
        self.radiobtn1.setIconSize(QtCore.QSize(40,40))
        self.radiobtn1.setFont(QtGui.QFont("Calibri",14))

        #connect radio button to method
        self.radiobtn1.toggled.connect(self.onRadioBtn)
        # add radio button to layout
        hboxLayout.addWidget(self.radiobtn1)

        # Create fuel economy button
        self.radiobtn2 = QRadioButton("Fuel Economy")
        self.radiobtn2.setIcon(QtGui.QIcon("images/fuel_icon.jpg"))
        # makes radio option the default checked
        # self.radiobtn2.setChecked(True)
        self.radiobtn2.setIconSize(QtCore.QSize(40,40))
        self.radiobtn2.setFont(QtGui.QFont("Calibri",14))

        #connect radio button to method
        self.radiobtn2.toggled.connect(self.onRadioBtn)
        # add radio button to layout
        hboxLayout.addWidget(self.radiobtn2)

        # Create Maintenance and Repair Radio Button
      
        self.radiobtn3 = QRadioButton("Maintenance and Repair")
        # makes radio option the default checked
        # self.radiobtn3.setChecked(True)
        self.radiobtn3.setIcon(QtGui.QIcon("images/maintenance_icon.jpg"))
        self.radiobtn3.setIconSize(QtCore.QSize(40,40))
        self.radiobtn3.setFont(QtGui.QFont("Calibri",14))

        #connect radio button to method
        self.radiobtn3.toggled.connect(self.onRadioBtn)
        # add radio button to layout
        hboxLayout.addWidget(self.radiobtn3)

        # Create RunCost radio button
        self.radiobtn4 = QRadioButton("Run Cost")
        # makes radio option the default checked
        # self.radiobtn4.setChecked(True)
        self.radiobtn4.setIcon(QtGui.QIcon("images/runcost_icon.png"))
        self.radiobtn4.setIconSize(QtCore.QSize(40,40))
        self.radiobtn4.setFont(QtGui.QFont("Calibri",14))

        #connect radio button to method
        self.radiobtn4.toggled.connect(self.onRadioBtn)
        # add radio button to layout
        hboxLayout.addWidget(self.radiobtn4)

        # Create Special Projects Button   
        self.radiobtn5 = QRadioButton("Special Projects")
        # makes radio option the default checked
        # self.radiobtn5.setChecked(True)
        self.radiobtn5.setIcon(QtGui.QIcon("images/special_projects_icon.png"))
        self.radiobtn5.setIconSize(QtCore.QSize(40,40))
        self.radiobtn5.setFont(QtGui.QFont("Calibri",14))

        #connect radio button to method
        self.radiobtn5.toggled.connect(self.onRadioBtn)
        # add radio button to layout
        hboxLayout.addWidget(self.radiobtn5)    


        # add groupbox to layout
        self.groupBox.setLayout(hboxLayout)

    def onRadioBtn(self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText(radioBtn.text())



    # slot
    @pyqtSlot( )
    def onStartStudy(self):
        if (self.label.text() == "Utilization"):
            self.label.setText("Start + Utilization button pressed")
            self.util_window = QtWidgets.QMainWindow()
            self.ui = HomeUtilizationUIClass()
            self.ui.setupUi(self.util_window)
            self.util_window.show()

        
        elif(self.label.text() == "Fuel Economy"):
            self.label.setText("Start + Fuel Economy button pressed")


        elif(self.label.text()== "Maintenance and Repair"):
            self.label.setText("Start + Maintenance and Repair button pressed")

        elif(self.label.text() == "Run Cost"):
            self.label.setText("Start + Run Cost button pressed")

        elif(self.label.text() == "Special Projects"):
            self.label.setText("Start + Special Projects button pressed")
            self.special_window = QtWidgets.QMainWindow()
            self.ui = SpecialProjectsClass()
            self.ui.setupUi(self.special_window)
            self.special_window.show()

        else:
            self.label.setText("Please make a selection to start study")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec_())    





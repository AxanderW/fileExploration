'''
Future improvements:
Hide and unhide windows not in use
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from specialprojects import Ui_SpecialProjectsMainWindow
import sys
from model import Model
from pandas_table import PandasModel
from consolidateFilesApp import ConsolidateFilesClass
from findFileApp import FindFileClass
from moveDirApp import MoveDirectoryClass
from copyDirApp import CopyDirectoryClass



class SpecialProjectsClass(Ui_SpecialProjectsMainWindow):
    def __init__(self):

        # initize super class
        super().__init__()
        self.model = Model()
        self.pandas_model = PandasModel()
        


    def setupUi(self, SMW):
        # Use super class initize setup
        super().setupUi(SMW)


    def debugPrint(self, msg):
        pass


    # slot
    def nextSlot(self):
        if(self.label_3.text() == "Find  File"):
            self.label_3.setText("Next + Find File")
            self.fileExplore_window = QtWidgets.QMainWindow()
            self.ui = FindFileClass()
            self.ui.setupUi(self.fileExplore_window)
            self.fileExplore_window.show()

        elif(self.label_3.text() == "Copy Directory"):
            self.label_3.setText("Next + Copy Directory")
            self.fileExplore_window = QtWidgets.QMainWindow()
            self.ui = CopyDirectoryClass()
            self.ui.setupUi(self.fileExplore_window)
            self.fileExplore_window.show()
        
        elif(self.label_3.text() == "Move Directory"):
            self.label_3.setText("Next + Move Directory")
            self.fileExplore_window = QtWidgets.QMainWindow()
            self.ui = MoveDirectoryClass()
            self.ui.setupUi(self.fileExplore_window)
            self.fileExplore_window.show()
        
        elif(self.label_3.text() == "Consolidate Files"):
            self.label_3.setText("Next + Consolidate Files")
            self.fileExplore_window = QtWidgets.QMainWindow()
            self.ui = ConsolidateFilesClass()
            self.ui.setupUi(self.fileExplore_window)
            self.fileExplore_window.show()        
        
        else:
            self.label_3.setText("Please select an option above")


    # slot
    def backSlot(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show() 


    # slot
    def onRadioSlot(self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label_3.setText(radioBtn.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SpecialProjectsClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exit(app.exec_())


    
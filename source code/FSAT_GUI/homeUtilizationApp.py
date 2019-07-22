from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from homeUtilization import Ui_DataViewMainWindow
import sys
from model import Model
from pandas_table import PandasModel

class HomeUtilizationUIClass(Ui_DataViewMainWindow):
    def __init__(self):

        # initize super class
        super().__init__()
        self.model = Model()
        self.pandas_model = PandasModel()

    def setupUi(self, DMW):
        # Use super class initize setup
        super().setupUi(DMW)



    def debugPrint(self, msg):

        self.debugtextBrowser.append(msg)


    
    def refreshAll(self):
        self.lineEdit_2.setText(self.model.getFileName())
    
    
    # slot
    def returnPressedSlot(self):
        self.debugPrint("RETURN key pressed")

        fileName = self.lineEdit_2.text()
        if self.model.isValid(fileName):
            self.model.setFileName(self.lineEdit_2.text())
            self.model.createDataFrame(fileName, self.sheetNamelineEdit.text())
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name! \n" + fileName)
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                |QtWidgets.QMessageBox.Cancel)

            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit_2.setText(" ")
            self.refreshAll()
            self.debugPrint("Invalid file specified: "+fileName)
    
    # slot
    def clearCustDataSlot(self):
        self.debugPrint("Clear Customer Data button pressed")

    # slot
    def loadDataPrevSlot(self):
        self.debugPrint("Load Data Preview button pressed")

        view = self.tableView_2
        fileName = self.lineEdit_2
        #sheetName = self.sheetNamelineEdit.text()
        dataframe = self.model.showDfPrev(fileName)
        self.pandas_model = PandasModel(dataframe)
        
        view.setModel(self.pandas_model)

        print(dataframe)

    
    # slot

    def loadDataFullSlot(self):
        self.debugPrint("Load Data Full button pressed")

        view = self.tableView_2
        fileName = self.lineEdit_2
        dataframe = self.model.showDfFull(fileName)
        self.pandas_model = PandasModel(dataframe)
        
        view.setModel(self.pandas_model)

        print(dataframe)



    # slot
    def backSlot(self):
       self.debugPrint("Back button pressed")


    # slot
    def browseSlot(self):
        self.debugPrint("Browse button pressed")
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
            self.model.createDataFrame(fileName, self.sheetNamelineEdit.text())
            self.refreshAll()

    # slot
    def downloadDataSlot(self):
        self.debugPrint("Download Data button pressed")

    # slot
    def cleanDataSlot(self):
        self.debugPrint("Clean Data button pressed")


    # slot
    def clearInvenDataSlot(self):
        self.debugPrint("Clear Inventory Data Button pressed")


    # slot
    def loadInvenDataPrevSlot(self):
        self.debugPrint("Load Inventory Data Preview button pressed")
        view = self.tableView_3


    # slot
    def loadInvenDataFullSlot(self):
        self.debugPrint("Load Inventory Data Full button pressed")
        view = self.tableView_3


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HomeUtilizationUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    
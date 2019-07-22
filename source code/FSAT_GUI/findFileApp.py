from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from specialprojects_secwindow import Ui_SpecialProjectsSecWindow
import sys
from model import Model
from pandas_table import PandasModel
from fileExplore_model import FileExploreModel
from os.path import expanduser



class FindFileClass(Ui_SpecialProjectsSecWindow ):
    def __init__(self):

        # initize super class
        super().__init__()
        self.model = Model()
        self.pandas_model = PandasModel
        self.file_model = FileExploreModel

    def setupUi(self, FMW):
        # Use super class initize setup
        super().setupUi(FMW)
        self.lineEdit_3.setText("Please leave field blank")
        self.label.setText("Special Projects: Find File")

    def debugPrint(self, msg):

        self.debugTextBrowser.append(msg)


    # slot
    def browseDirSlot(self):
        self.debugPrint("Browse Directory button pressed")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        dirName = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "QFileDialog.getExistingDirectory",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )

        if dirName:
            self.debugPrint("setting directory name: "+dirName)
            self.lineEdit.setText(dirName)

    # slot
    def browseTargetSlot(self):
        self.debugPrint("Browse Target Directory button pressed")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        targetName = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "QFileDialog.getExistingDirectory",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )

        if targetName:
            self.debugPrint("setting directory name: "+targetName)
            self.lineEdit_2.setText(targetName)


    # slot
    def browseFileSlot(self):
        self.debugPrint("Browse File button pressed")
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
            self.lineEdit_3.setText(fileName)
            #self.model.createDataFrame(fileName, self.sheetNamelineEdit.text())
            #self.refreshAll()


    
    # slot
    def releasePresedSlot(self):
        self.debugPrint("Return key pressed")


    # slot
    def executeSlot(self):


        self.debugPrint("Executing Process")
        rootdir = self.lineEdit.text()
        file_name = self.lineEdit_4.text()

        if rootdir != '' and file_name != '':
            try:
                self.debugPrint("Finding file: {} in Directory location: {}".format(file_name, rootdir))
                file_locations = self.file_model.findFile(self,rootdir,file_name)
                self.debugPrint("File Name: {} found in locations below: \n{}".format(rootdir,file_locations))
            except:
                self.debugPrint("Please enter a valid Root Directory and File Name")
        
        elif rootdir == '' or file_name == '':
            self.debugPrint("Please enter both a Root Directory and File name")
            self.debugPrint("Current Root Directory entered: {}\nCurrent File name entered: {}".format(rootdir,file_name))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FindFileClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
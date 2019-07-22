from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from specialprojects_secwindow import Ui_SpecialProjectsSecWindow
import sys
from model import Model
from pandas_table import PandasModel
from fileExplore_model import FileExploreModel
from os.path import expanduser



class ConsolidateFilesClass(Ui_SpecialProjectsSecWindow ):
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
        self.label.setText("Special Projects: Consolidate Files")


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
        targetfolder = self.lineEdit_2.text()

        if rootdir != '' and file_name != '' and targetfolder != '':
            try:
                self.debugPrint("Consildating all files with name: {} located in Directory location: {}".format(file_name, rootdir))
                consolidated_file = self.file_model.findConsolidFile(self,rootdir,file_name,targetfolder)
                self.debugPrint("Files successfully consolidated and can be found: \n{}".format(targetfolder))
            except:
                self.debugPrint("Please enter a valid Root Directory and File Name")
        
        elif rootdir == '' or file_name == '' or targetfolder == '':
            self.debugPrint("Please enter Root Directory, File name, and Target Directory")
            self.debugPrint("Current Root Directory entered: {}\nCurrent File name entered: \n{}Current Target Folder name: {}".format(rootdir,file_name,targetfolder))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ConsolidateFilesClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
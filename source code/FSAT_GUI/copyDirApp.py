from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from specialprojects_secwindow import Ui_SpecialProjectsSecWindow
import sys
from model import Model
from pandas_table import PandasModel
from fileExplore_model import FileExploreModel
from os.path import expanduser



class CopyDirectoryClass(Ui_SpecialProjectsSecWindow ):
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
        self.label.setText("Special Projects: Copy Directory")


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

        ''' NOTE WHEN COPYING A ROOT FILE TO A TARGET FILE
        The target file has to be a brand new directory name '''

        self.debugPrint("Executing Process")
        rootdir = self.lineEdit.text()
        targetfolder = self.lineEdit_2.text()

        if rootdir != '' and targetfolder != '':
            try:
                self.debugPrint("Copying directory: {} to Target location: {}".format(rootdir,targetfolder))
                self.file_model.copyDirectory(self,rootdir,targetfolder)
                self.debugPrint("Directory: {} successfully copied to Target location: {}".format(rootdir,targetfolder))
            except:
                self.debugPrint("Please enter a new Target Folder name that does not already exist")
        
        elif rootdir == '' or targetfolder == '':
            self.debugPrint("Please enter both a Root Directory and Target Directory")
            self.debugPrint("Current Root Directory entered: {}\nCurrent Target Direcotry entered: {}".format(rootdir,targetfolder))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CopyDirectoryClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
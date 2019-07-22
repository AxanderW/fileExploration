# import dependencies

import shutil
import os
import pandas as pd
import numpy as np
import csv
import glob
from shutil import copyfile
from sys import exit



class FileExploreModel:
    def __init__(self):
        self.fileName = None
        self.combined_excel = []
        self.RootDir = ""
        self.TargetFolderTest = ""




    def getSrcFolder(self):
        self.RootDir = str(input("Enter Root Directory with full path name: "))
        return self.RootDir



    def getTargetFolder(self):
        self.TargetFolder = str(input("\nEnter Target Folder with full path name: "))
        return self.TargetFolder

    def getFileName(self):
        fileName = str(input("\nEnter Filename: "))
        return fileName
    

    def copyDirectory(self,rootdir,targetfolder):
        print("\nCopying directory: {} in progress...".format(rootdir))
        shutil.copytree(rootdir, targetfolder)
        print("\nDirectory successfully copied from {} to Target location: {}".format(rootdir,targetfolder))
    
    
    def moveDirectory(self,rootdir,targetfolder):
        print("\nMoving rootdirectory: {} in progress..".format(rootdir))
        shutil.move(rootdir, targetfolder)
        print("\nDirectoy successfully moved from {} to Target location: {}".format(rootdir,targetfolder))

    
    def findFile(self, rootdir,filename):
        file_locations = []
        print("\nSearching for files with name: {} in rootdirectory: {}".format(filename,rootdir))
        print("\nFiles with name: {} found in locations below: \n".format(filename))
        for root,dirs, files in os.walk((os.path.normpath(rootdir)), topdown=False):
            for name in files:
                if name.startswith(filename):
                    print("----------------------")
                    print("Found")
                    SourceFolder = os.path.join(root,name)
                    file_locations.append(SourceFolder)
                    print(SourceFolder)
        return file_locations




    def findConsolidFile(self,rootdir,filename,targetfolder):
        combined_excel = []
        print("Searching for files with name: {} in rootdirectory: {} \n\nConsolidated file will out to location: {}\n".format(filename,rootdir,targetfolder))
        for root,dirs, files in os.walk((os.path.normpath(rootdir)), topdown=False):
            for name in files:
                if name.startswith(filename):
                    print("-----------------")
                    print("Found")
                    SourceFolder = os.path.join(root,name)
                    #shutil.copy2(SourceFolder,TargetFolder) # comment this line out to perform another function
                    print(SourceFolder)
                    combined_excel.append(SourceFolder)
        #print(combined_excel)
        
        
        print("\nConsolidating files with name: {} in progress..".format(filename))
        consolidated_files = pd.concat(pd.read_excel(f, sort=False) for f in combined_excel)
        print("\nConsolidating complete")
        print("\nExporting file...")
        
        
        consolidated_files.to_excel("{}/Consolidated_File.xlsx".format(targetfolder),
                                    sheet_name = 'CONSOLIDATED_FILE', na_rep = '',
                                    float_format = "%.0f",
                                    header=True, index=False)


        print("\nExport complete")
        print("\nFile Preview: \n\n")
        print(consolidated_files.head())
        return consolidated_files 
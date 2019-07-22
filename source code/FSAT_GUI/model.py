import pandas as pd 
import shutil
import os
import numpy as np
import csv
import glob
from shutil import copyfile
from sys import exit



class Model:
    def __init__(self):
        self.fileName = None
        self.fileContent = ""
        self.sheetName = None
        self.dataframe = None


    def isValid(self, fileName):
        try:
            file = open(fileName, 'r')
            file.close()
            return True

        except:
            return False

    def setFileName(self, fileName):
        if self.isValid(fileName):
            self.fileName = fileName
            #self.fileContents = open(fileName, 'r').read()
        else:
            #self.fileContents = " "
            self.fileName = ""

    def getFileName(self):
        return self.fileName


    def getFileContents(self):
        return self.fileContents


    def createDataFrame(self, fileName, sheetName):
        if self.isValid(fileName):
            self.dataframe = pd.read_excel(fileName,sheet_name  =sheetName)

            return self.dataframe
        


    def showDfPrev(self,fileName):
        return self.dataframe.head(10)



    def showDfFull(self,dataframe):
        return self.dataframe


    def getColumns(self,fileName,sheetName):
        self.dataframe = self.createDataFrame(fileName,sheetName)
        self.columns = []
        for col in self.dataframe.columns:
            col = str(col)
            self.columns.append(col)
    

        return self.columns


    def getFleetColsUsable(self, all_col_list, restricted_col_list):
        useable_list = []
        for col in all_col_list:
            if (col not in restricted_col_list):
                useable_list.append(col)
        return useable_list



    def getFleetColsAll(self):
        fleet_list_all = ['UNIT', 'UPLOAD_DATE', 'CURRENT_DATA', 'ACTIVE_UNIT', 'COMPANY_NAME',
       'SIC', 'SIC_INDUSTRY', 'NAICS', 'NAICS_INDUSTRY', 'VIN', 'MODEL_YEAR',
       'MY_Checker', 'MAKE', 'MODEL', 'TYPE', 'CITY', 'REGION', 'STATE',
       'SUB_LOC', 'DC', 'LICENSE', 'STATE_REG', 'USE_TYPE', 'DESCRIPTION',
       'FRT_TYPE', 'INSERVICE_DATE', 'DAYS_IN_SERVICE', 'MONTHS_IN_SERVICE',
       'YEARS_IN_SERVICE', 'OD_READING', 'ODREADING_DATE',
       'AVG_ANNUAL_MILEAGE', 'LAST12_MO_MILEAGE', 'LAST12_MO_FINANCE',
       'Max OD']

        return fleet_list_all



    def getFleetColsRestricted(self):
        fleet_list_restricted = [
                            'MY_Checker',
                            'DAYS_IN_SERVICE',
                            'MONTHS_IN_SERVICE',
                            'YEARS_IN_SERVICE',
                            'AVG_ANNUAL_MILEAGE',
                            'LAST12_MO_MILEAGE',
                                'Max OD']
        return fleet_list_restricted


    def getFleetColsUseable(self):

        fleet_cols_useable = ['UNIT', 'UPLOAD_DATE', 'CURRENT_DATA', 'ACTIVE_UNIT',
                     'COMPANY_NAME', 'SIC', 'SIC_INDUSTRY', 'NAICS', 'NAICS_INDUSTRY',
                      'VIN', 'MODEL_YEAR', 'MAKE', 'MODEL', 'TYPE', 'CITY', 'REGION', 'STATE', 
                      'SUB_LOC', 'DC', 'LICENSE', 'STATE_REG', 'USE_TYPE', 'DESCRIPTION', 'FRT_TYPE', 
                      'INSERVICE_DATE', 'OD_READING', 'ODREADING_DATE', 'LAST12_MO_FINANCE']
        return fleet_cols_useable



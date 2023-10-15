import pandas as pd

'''
A simple spreadsheet reader class. Returns specific column entries
meaningful for AATG registration. Currently hard-coded based on the spreadsheet template
'''
class Reader:
    def __init__(self, pathSpreadSheet):
        self.SpreadSheetPath = pathSpreadSheet
        
    def ReadSpreadSheet(self):
        self.StudentRecords = pd.read_excel(self.SpreadSheetPath)
    
    def GetNumberOfRecords(self):
        return self.StudentRecords.shape
    
    def GetIthRowRecord(self, row):
        #'StudentFirstName', 'StudentLastName', 'StudentGSSBEmail', 'LingcoPwd', 'StudentCode'
        return self.StudentRecords.loc[row, ['StudentFirstName', 'StudentLastName',
                                             'StudentGSSBEmail', 'LingcoPwd',
                                             'StudentCode']]
        
        

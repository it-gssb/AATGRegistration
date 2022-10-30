import argparse
import AATGRegistrationManager
import SpreadSheetReader

'''
Entry function for AATG registration
'''

def parseArguments():
    parser = argparse.ArgumentParser(description='Read student data from spreadsheet.')
    parser.add_argument('--studentSpreadSheetPath', dest='studentSpreadSheetPath', action='store',
                        type=str, required=True, help='Full path of spreadsheet containing student records.')
    parser.add_argument('--schoolURL', dest='schoolURL', action='store',
                        type=str, required=True, help='URL of school')
                        
    args = parser.parse_args()
    return (args.studentSpreadSheetPath, args.schoolURL)
    
def registerAllStudentsInLingco(spreadSheetPath, schoolURL):    
    reader = SpreadSheetReader.Reader(spreadSheetPath)
    reader.ReadSpreadSheet()
    numRows, numCols = reader.GetNumberOfRecords()

    testManager = AATGRegistrationManager.Manager(schoolURL)
    for iRow in range(numRows):
        aRecord = reader.GetIthRowRecord(iRow)
        testManager.RegisterAStudent((aRecord.StudentFirstName, aRecord.StudentLastName, aRecord.StudentGSSBEmail, aRecord.LingcoPwd, aRecord.StudentCode))
    
if __name__ == "__main__" :    
    args = parseArguments()
    registerAllStudentsInLingco(args[0], args[1])
    
    
#usage python AATGRegistration.py --studentSpreadSheetPath "../data/AATG-Template-2022.xlsx" --schoolURL "www.gssb.org" 


import requests

''' Following command works.
curl -X POST -k -H "Accept:application/json,text/plain,*/*" -H "Content-Type:application/json" -i "https://class.lingco.io/api/users/register" --data "{\"first_name\":\"Test3\",\"last_name\":\"Test\",\"language\":\"de\",\"email\":\"test3@test.com\",\"account_type\":\"student\",\"instructor_code\":\"\",\"password\":\"abcd1234\",\"missing_school_url\":\"www.test.com\",\"organization_id\":40427, \"registration_token\":\"\",\"course_code\":null}"
'''

'''
A class which registers a student in Lingco system
Success/failure is indicated by a logging statement and status code from response.
'''
class Manager:
    def __init__(self, schoolURL):
        self.schoolURL = schoolURL
        self.mainURL = "https://class.lingco.io/api/users/register"
        self.headerInfo = {"Accept":"application/json,text/plain,*/*", "Content-Type":"application/json"}
        
        urlForUnregisteredSchool = "https://class.lingco.io/api/organizations/not_found"
        response = requests.get(urlForUnregisteredSchool, headers=self.headerInfo)
        self.organizationID = response.json()['id']
        
    def RegisterAStudent(self, studentRecord):
        firstName, lastName, emailId, studentPasswd, studentCode = studentRecord
        studentInfo = {"first_name":firstName,"last_name":lastName,"language":"de","email":emailId,
         "account_type":"student","instructor_code":"","password":studentPasswd,
         "missing_school_url":self.schoolURL,"organization_id":self.organizationID,
         "registration_token":"","course_code":None}
         
        response = requests.post(self.mainURL, headers=self.headerInfo, json=studentInfo)
        print('StudentEmail = {2}, StudentCode = {3}, Status code = {0} and message = {1}'.format(response.status_code, response.text, emailId, studentCode) )
        

       
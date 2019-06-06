import sys
import win32com.client
import pytest
import datetime
import test_generator as tGen
import test_hashgrinder as tHash
import test_pagan as tPagan
import test_pgnreader as tPgn

emailSubject = ""
emailBody = ""

#Get the arguments from CLI
if(len(sys.argv) == 2):
    numberLoop = sys.argv[1]
    emailResultTo = None
    shoudlIEmail = False
elif(len(sys.argv) == 1):
    numberLoop = 1
    emailResultTo = None
    shoudlIEmail = False
else:
    numberLoop = sys.argv[1]
    emailResultTo = sys.argv[2]
    shoudlIEmail = True

numberLoop =int(numberLoop)

#Runs Default Pytest Module
def runPytest():
    if(pytest.main(['--resultlog=emailBody.txt'],plugins=None)):
        return True
    else:
        return False

def makeEmail(to, title, body):
    olMailItem = 0
    ol = win32com.client.Dispatch("Outlook.Application")
    msg = ol.CreateItem(olMailItem)
    msg.To = to
    msg.Subject = title
    msg.Body = body
    msg.Send()
    ol.Quit()
    
def sendEmail(eSubj):
    emailFile = open("emailBody.txt", "r")
    body = ""
    for line in emailFile:
        body += line
    
    makeEmail(emailResultTo, eSubj, body)


#Main Driver Method
def runTests():
    #For number of loops run the pytest suite
    timeStart = datetime.datetime.now()
    for tests in range(0, numberLoop):
        if(runPytest()):
            emailSubject = "FAIL"
        else:
            emailSubject = "PASS"
    timeEnd = datetime.datetime.now()

    if(shoudlIEmail):
        sendEmail(emailSubject)
    
    print("Time Started:", timeStart)
    print("Time Ended:", timeEnd)
    
#Bottom Run
runTests()
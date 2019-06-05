import sys
import smtplib
import email
import pytest
import test_generator as tGen
import test_hashgrinder as tHash
import test_pagan as tPagan
import test_pgnreader as tPgn

server = smtplib.SMTP('smtp.gmail.com', 587)

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


def sendEmail():
    emailFile = open("emailBody.txt", "r")
    body = ""
    for line in emailFile:
        body = emailBody + line
    
    fromaddr = "marcelli@seattleu.edu"
    toaddr = emailResultTo
    msg = body

    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("vmarcelli.pop@gmail.com", "VmP0pP455")
    server.sendmail(fromaddr, toaddr, msg)
    server.close()


def runTests():
    for tests in range(0, numberLoop):
        if(not runPytest()):
            emailSubject = "FAIL"
        else:
            emailSubject = "PASS"

    if(shoudlIEmail):
        sendEmail()
    
    


runTests()
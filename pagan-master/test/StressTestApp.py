'''
Runs the test suite in parallel x number of times

'''
import os
import sys
import datetime

#Get the arguments from CLI
paramIn = sys.argv[1]
numofTimes = int(paramIn)
command = "python runTestSuite.py 10 &"

timeStart = datetime.datetime.now()
for num in range(0, numofTimes):   
    os.system(command)
timeEnd = datetime.datetime.now()

print("Input parallels used for StressTest:", numofTimes)
print("Number of times runTestSuite was used: 10")
print("Time started:", timeStart)
print("Time ended:", timeEnd)



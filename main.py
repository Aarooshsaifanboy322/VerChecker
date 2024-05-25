# Version Checker
# File made by AarooshCoding33

# Credits: AarooshCoding33, Snakyguy, GamingLegend, TheBLOXFRUITSPlr533, TheTSBSafwan_Boy93022
# Helpers: Snakyguy, GamingLegend, TheBLOXFRUITSPlr533, TheTSBSafwan_Boy93022

# © 2024 E-Coders Team
# All Rights Reserved

import time as tm
import os

os.chdir("/Users/amranhossain/Desktop/")

def startfile():
    # File starter
    start = "Version checker\n© 2024 E-Coders Team\nAll rights reserved."
    return start
def getData(data1, data2, data3):
    # Data Collector
    SizeOfData = data1 + data2 + data3
    return SizeOfData

# Data
data1 = "8127645789723649283489219829387452536455235432453462377508346572790499816645625678718836461284729834623848"
data2 = "237428390487672398589885278915987585278919238748293488237466545555452784781276546271712228267541278457756267385746564646"
data3 = ""

startProgram = startfile()
print(startProgram)
tm.sleep(4)
fileName = input("Your file name please: ")
try:
    fileOpen = open(fileName)
    print("Getting version data...")
    tm.sleep(3)
    dataCollector = getData(data1, data2, data3)
    totalData = dataCollector
    def show():
        print("Displaying in few seconds...")
        tm.sleep(7)
        print("Sorry, system got damaged while displaying version. Please try again in 3 hours.")
        tm.sleep(4)
        print("Repairing system...")
        tm.sleep(10800)
        exit()
    VersionShow = show()
except FileNotFoundError:
    print("File does not exist.")

if True:
    # Virus injector
    code = "SS Virus"
    code.virusInject()
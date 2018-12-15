# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 10:31:46 2018

@author: huesca12
"""
import os
#####################
####VARIABLE INIT####
#####################
newTrackBuilt   = True
yearEvent       = False
yearHadEvent    = False
nextYearKey     = "n"
viewLinesKey    = "l"
viewInfoKey     = "i"
affResponses    = ["yeah", "sure", "ok", "yes", "Yes", "Yeah", "Sure", "Ok", "y", "Y", "s", "S"]
startQuery      = "Press [s] to start\n"
version         = "v0.0.1alpha\n\n"
menuResponse    = ""
author          = "Developed by: Nicolas Casey"
menuContent     = "Type the key that corresponds to what you want to do: \n#################################\n# " + nextYearKey + " # Continue to the next year #\n#################################\n# " + viewLinesKey + " # View your lines           #\n#################################\n# i # View company info         #\n#################################\n\nInput: "
currentYear     = 1864
IyearASCII      = [" #### " , "  #  ", " ### " , " #### " , "  # # " , "######" , " #### " , "######" , " #### ", " #### "]
IIyearASCII     = ["##   #" , "# #  ", "#   #" , "#    #" , " #  # " , "#     " , "#     " , "    # " , "#    #", "#    #"]
IIIyearASCII    = ["# ## #" , "  #  ", "   # " , "   ## " , "######" , "##### " , "# # # " , "   #  " , " #### ", " #### "]
IVyearASCII     = ["#   ##" , "  #  ", "  #  " , "#    #" , "    # " , "     #" , "#    #" , "  #   " , "#    #", "   #  "]
VyearASCII      = [" #### " , "#####", "#####" , " #### " , "    # " , "##### " , " #### " , " #    " , " #### ", "  #   "]
playerLines     = []
historicalLines = ["District"]
historicalDates = [1864]
startingCash    = 100000
cash            = startingCash
companyName     = "Metropolitan Railway"
devMsg          = "LTS is in active development with nightly builds.\nCheck the github repository @ https://github.com/huesca12/londonTransport for the latest version!"
#####################
##Program Functions##
#####################
def yearMaker(year):
    yearList = [int(i) for i in str(year)]
    temporary1 = ""
    temporary2 = ""
    temporary3 = ""
    temporary4 = ""
    temporary5 = ""
    for j in yearList:
        temporary1 = temporary1 + IyearASCII[j]   + " "
        temporary2 = temporary2 + IIyearASCII[j]  + " "
        temporary3 = temporary3 + IIIyearASCII[j] + " "
        temporary4 = temporary4 + IVyearASCII[j]  + " "
        temporary5 = temporary5 + VyearASCII[j]   + " "
        temporary  = temporary1 + "\n" + temporary2 + "\n" + temporary3 + "\n" + temporary4 + "\n" + temporary5 + "\n"
    return temporary

def eventPrefixer():
    global yearHadEvent
    if yearEvent == True and yearHadEvent == False:
        print("Events:\n")
        yearHadEvent = True

def lineHasTracksBuilt(lineName):
    if lineName == "District":
        return True
    
def newTrackBuiltChecker():
    if currentYear in historicalDates and lineHasTracksBuilt(historicalLines[historicalDates.index(currentYear)]) == True:
        global yearEvent
        yearEvent = True
        newLineName = historicalLines[historicalDates.index(currentYear)]
        playerLines.append(newLineName)
        eventPrefixer()
        print("A new line (" + newLineName + ") has been built.\n")
         
def nextYear():
    global currentYear
    global yearHadEvent
    currentYear += 1
    yearHadEvent = False
    print(currentYear)
    print(yearMaker(currentYear))
    newTrackBuiltChecker()
    menuGenerator()
    
    
def titleScreen():
    print("#	 ####  #     # # #    ####  #     #\n#	#    # ##    # #   # #    # ##    #\n#	#    # #  #  # #   # #	  # #  #  #\n#       #    # #    ## #   # #	  # #    ##\n#######  ####  #     # # #    ####  #     #\n")
    print("####### # # #   #####  #     #  ##### # #    ####  # # #  #######\n   #	#    # #     # ##    # #      #   # #    # #    #    #\n   #	# # #  # # # # #  #  #  ####  # #   #    # # # #     #\n   #	#   #  #     # #    ##      # #     #    # #   #     #\n   #	#    # #     # #     # #####  #      ####  #    #    #\n")
    print(" ##### ####### #     #\n#         #    ##   ##\n ####     #    # # # #\n     #    #    #  #  #\n#####  ####### #     #\n")
    print(author)
    print(version)
    print(devMsg)
    startResponse = input(startQuery)
    
    if startResponse in affResponses:
        startGame()

def startGame():
    os.system('cls||clear')
    print("[1860]: By Act of Parliament and Decree of HM Queen Victoria you are made Commissioner of the Metrpolitan Railway,\n and tasked with connecting the Paddington and Farringdon Street rail stations via underground rail link.")
    print("[1863]: On January 9, 1863, the world's first underground railway is unveiled connecting the two stations in addition to 5 other stops.\n 38,000 people rode the innaugural trains.\n\n")
    print(yearMaker(currentYear))
    newTrackBuiltChecker()
    menuGenerator()

def linesInterface():
    print("\n\n\nYour Lines:\nType v to view and edit line details.\nType e to return to the main menu.\n\n")
    for i in playerLines:
        x = 1
        print("#################################\n# " + str(x) + " # " + i + "\n#################################\n\n")
    lineCommand = input("Input: ")
    linesTerminal(lineCommand)

def infoTerminal(command):
    global companyName
    if command == "e":
        menuGenerator()
    
    elif command == "r":
        companyName = input("Type new name:")
        infoInterface()

def infoInterface():
    print("\n\nType r to rename company. Type e to return to the main menu.")
    print("#################################\nCompany: " + companyName + "\n\nCash(£):" + str(cash) + "\n")
    infoCommand = input("Input: ")
    infoTerminal(infoCommand)

def menu(userInput):
    if userInput == nextYearKey:
        nextYear()
        
    elif userInput == viewLinesKey:
        linesInterface()
        
    elif userInput == viewInfoKey:
        infoInterface()
        
    else:
        menuGenerator()
        
def menuGenerator():
 menuResponse=input(menuContent)
 menu(menuResponse)
 
def linesTerminal(command):
    if command == "v":
        lineNumber = input("Enter line number: ")
    
        intLineNumber = int(lineNumber)
        selectedLine = playerLines[intLineNumber - 1]
        print("#################################\n" + selectedLine + " Line\n\nType r to rename the line. Type e to return to the line list.")
        subLineCommand = input("Input: ")
        
        if subLineCommand == "r":
            newName = input("Type new name: ")
            playerLines[intLineNumber - 1] = newName
            linesInterface()
            
        if subLineCommand == "e":
            linesInterface()
            
    if command == "e":
        menuGenerator()
            
            
    
############    
titleScreen()

#This file is for the command line prototype
from QuadraticEquation import *
from LinearEquation import *
from FileSorter import * 
from Logarithms import *

#This function starts and runs the command line and checks the use input for commands.
def callcommand():

    command = input(": ") #This is the where the user inputs their commands  

    if command.startswith("help"):
        print("Help Guide:\n-Inbuilt help TBA, go to Github page for help.\n")

    if command.startswith("solve"): #Checks for math-related commands

        command2 = command.replace("solve", "")

        if command2.startswith(" QE"): solveQE()
        if command2.startswith(" slope"): slopesolve()            
        if command2.startswith(" intercept"): interceptsolve()
        if command2.startswith(" log"): solveLog()
  
    if command.startswith("file"): #This if statement checks for file-related commands.
        command2 = command.replace("file", "")
        if command2.startswith(" sort"): sort_files()
            
    if command == "end": quit()
    else: print("Not a valid argument")
        
    callcommand() 
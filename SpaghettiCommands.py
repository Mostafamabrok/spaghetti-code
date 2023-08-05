#This file is for the command line prototype
from QuadraticEquation import *
from LinearEquation import *
from FileSorter import * 
from Logarithms import *


#This function starts and runs the command line and checks the use input for commands. NOTE: Better system needed
def callcommand():
    #This is the where the user inputs their commands
    command = input(": ")
    
#    arguments = {
#        "solve" : [QE, "slope", "intercept"],
#        "file" : ["sort"]
#        }

#    for start_arg in arguments.keys():
#       if command.startswith(start_arg):
#            pass

    #These if statements check for commands by checking what word is written at the start. When it finds a command associated with the word it removes the word and goes on to the next word
    if command.startswith("help"):
        print("Help Guide: \n -An inbuilt help guide for the command line interface is TBA, for more info, go to the Github repo page")
    #This if statement checks for math commands
    if command.startswith("solve"):
        command2 = command.replace("solve", "")
        if command2.startswith(" QE"):
            solveQE()
            callcommand()
        
        if command2.startswith(" slope"):
            slopesolve()
            callcommand()
            
        if command2.startswith(" intercept"):
            interceptsolve()
            callcommand()
            
        if command2.startswith(" log"):
            solveLog()
            callcommand()
        
        
    #This if statement checks for file category commands        
    if command.startswith("file"):
        command2 = command.replace("file", "")
        if command2.startswith(" sort"):
            sort_files()
            callcommand()
    
    if command == "end":
        quit()
    
    else:
        print("Not a valid argument")
        callcommand()
    
            
    

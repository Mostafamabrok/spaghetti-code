#This file is for the command line prototype
from QuadraticEquation import *
from LinearEquation import *
from FileSorter import * 
 
def callcommand():
     
    command = input(": ")
    
    if command.startswith("help"):
        print("Help Guide: \n -An inbuilt helpguide for the command line interface is TBA, for more info, go to the Github repo page")
    
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
            
    if command.startswith("file"):
        command2 = command.replace("file")
        if command2.startswih(" sort"):
            sort_files()
            callcommand()
            
    

callcommand()
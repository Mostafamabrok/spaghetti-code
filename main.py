import math
import matplotlib.pyplot as plt
import numpy as np
import shutil
import os
from QuadraticEquation import *
from LinearEquation import *
from FileSorter import *

project_name = "PROJECTNAME!"

def listmathprograms():
    print("1-Quadratic Equation solving tool")
    print("2-Solve for Slope using 2 points")
    print("3-Solve for X or Y intercept")
    
    chosenprogram = input("")
    
    if chosenprogram == "1":
        solveQE()
        welcome()
    if chosenprogram == "2":
        slopesolve()
        welcome()
    if chosenprogram == "3":
        interceptsolve()
        welcome()
        
def listfileprograms():
    print("1-Directory Sorter (will sort your files into folders)")
    chosenprogram = input("")
    if chosenprogram == "1":
        sort_files()
        welcome()

def welcome():
    print("Welcome to the " + project_name)
    program_catergory = input("Math Programs or File Programs (m/f)")
    print("\nPlease Select the program you would like to use by pressing the respective number and pressing enter.\n")
    if program_catergory == "m":
        listmathprograms()
        
    if program_catergory == "f":
        listfileprograms()
    
    else:
        "Please input in the correct format in lowercase, try again."
        

welcome()
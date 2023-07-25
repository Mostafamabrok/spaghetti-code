import math
import matplotlib.pyplot as plt
import numpy as np
from QuadraticEquation import *
from LinearEquation import *

project_name = "Project NAME!"

def listprograms():
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

def welcome():
    print("Welcome to the " + project_name)
    print("\nPlease Select the program you would like to use by pressing the respective number and pressing enter.\n")
    listprograms()

welcome()
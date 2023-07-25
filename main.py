import math
import matplotlib.pyplot as plt
import numpy as np
from QuadraticEquation import *

project_name = "Project NAME!"

def listprograms():
    print("1-Quadratic Equation solving tool")
    print("2-PLACEHOLDER")
    print("3-PLACEHOLDER\n")
    
    chosenprogram = input("")
    
    if chosenprogram == "1":
        solveQE()
        welcome()

def welcome():
    print("Welcome to the " + project_name)
    print("\nPlease Select the program you would like to use by pressing the respective number and pressing enter.\n")
    listprograms()

welcome()
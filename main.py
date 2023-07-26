import math
import matplotlib.pyplot as plt
import numpy as np
import shutil
import os
from SpaghettiCommands import *
from QuadraticEquation import *
from LinearEquation import *
from FileSorter import *

#self explanatory 
project_name = "Spaghetti Project"

#Runs the CLI from SpaghettiCommands
def welcome():
    print("Welcome to the " + project_name)
    callcommand()

        
#Starts the entire program
welcome()
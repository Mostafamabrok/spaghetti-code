import math
import matplotlib.pyplot as plt
import numpy as np

#This function can only solve one type of logarithm problem
#More Types of probelms will be added

def solveLog():
    print("Welcome to the Logarithm Solver!")
    log_base = int(input("Input the Logarithmic base (the little number next to the 'Log'):"))
    argument = int(input("Input the number next to the logarithmic base: "))
    #Uses math and the previous two inputs to calculate the solution to Log_b(b^x) = x
    solution = math.log(argument, log_base)
    print("\nLog_"+str(log_base) + "("+ str(argument) + ")" + "="  + str(solution))
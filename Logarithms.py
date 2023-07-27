import math
import matplotlib.pyplot as plt
import numpy as np

def solveLog():
    print("Welcome to the Logarithm Solver!")
    log_base = int(input("Input the Logarithmic base (the little number next to the 'Log'):"))
    log_base2 = int(input("Input the number next to the logarithmic base: "))
    solution = math.log(log_base2, log_base)
    print("\nLog_"+str(log_base) + "("+ str(log_base2) + ")" + "="  + str(solution))


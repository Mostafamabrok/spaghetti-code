def solveQE(): 
 import math
 import matplotlib.pyplot as plt
 import numpy as np

 print("WELCOME TO TO THE ES (Liner/Quadratic Equation solver)\n")

 print("(Copyright of Mostafa.INC, Developed by by Mostafa Studios)\n")

 print("Let's get started, type your variables!\n")

 #Asking the user to set their A, B, and C variables
 a = float(input("Set your 'A' variable:"))
 b = float(input("Set your 'B' variable:"))
 c = float(input("Set your 'C' variable:"))

 #Mathematical operations for Quadratic Equations
 if (b*b - 4*a*c) > 0 :
  x_one = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
  x_two = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
  vertex = -(b/(2*a))
 #Displaying the Solution for the Quadratic Equation
  print("The first solution is:")
  print(x_one)
  print("\n")
  print("The second solution is:")
  print(x_two)
  print("")
  print(vertex)

 else:
  print("The routes are imaginary, we didnt have the funding to include that.")

 #Asking for persmission to plot the equation
 plotpermission = input("Do you want to plot your quadratic equation (y/n): ")

 if plotpermission == "y" :
  print("Undergoing plotting process...\n")
  print("Plotted!")
#Setting up plotting variables
  x_plot = np.linspace(-10, 10,100)
  y_plot = a*(x_plot**2) + b*x_plot + c
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  plt.plot(x_plot, y_plot, 'r')
  plt.show()
  print("Thank you for using the QES!")

 else:
  print("Thank you for using the QES!\n")
  

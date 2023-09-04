def slopesolve():
    print("This program will help you easily obtain the slope of a given line.")
    print("Type the respective coordinates in the following prompts.\n")
    x1= int(input("X of the first point: "))
    y1= int(input("Y of the first point: "))
    x2= int(input("X of the second point: "))
    y2= int(input("Y of the second point: "))
    slope=(y2-y1)/(x2-x1)
    print("\n Your slope is:" + str(slope) + " !")
    
def solve_x_intercept():
    y_int_slope = int(input("Slope of the line: "))
    x= int(input("\nX of the point: "))
    y= int(input("Y of the point: "))
    y_int = y-(x*y_int_slope)
    x_int = y_int_slope*0+y_int
    print("The x intercept of this line is: " + str(x_int))

def solve_y_intercept():
    y_int_slope = int(input("Slope of the line: "))
    x= int(input("\nX of the point: "))
    y= int(input("Y of the point: "))
    y_int = y-(x*y_int_slope)
    print("The y intercept of this line is: " + str(y_int))
    
def interceptsolve():
    xory = input("Would you like to solve for x-intercept or y-intercept (x/y): ")
    
    if xory == "x":
        solve_x_intercept()
    
    if xory == "y":
        solve_y_intercept()
        

    
   
    
    


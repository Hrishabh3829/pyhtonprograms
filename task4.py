# Python Program to Solve Quadratic Equation 
import math
a=int(input("coefficient of x^2:"))
b=int(input("coefficient of x:"))
c=int(input("enter constant:"))
d=(-b+(math.sqrt(math.pow(b,2)-4*a*c)))/(2*a)
e=(-b-(math.sqrt(math.pow(b,2)-4*a*c)))/(2*a)
print("solution:",d,e)
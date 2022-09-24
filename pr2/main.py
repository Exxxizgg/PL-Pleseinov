import math
x = float(input("x"))
y = float(input("y"))
z = float(input("z"))
s = (math.e **(math.fabs(x - y))) * ((math.fabs (x - y)) **(x + y)) / (math.atan(x) + math.atan(z)) + (x**6 + math.log(y)**2)**(1/3)
print("s= {0:.4f}".format (s))

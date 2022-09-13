import math
x = int(input("Введите значение"))
t = int(input("Введите значение"))
m = int(input("Введите значение"))
z = ((6 * math.pi * t + 10 * math.cos(x ** 2)) / (math.sin(x) - (math.sqrt(t)))) * m ** 6
print("z = {0:.2f}".format(z))

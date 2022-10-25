import math
print ("Прямоугольник : 1; треугольник : 2; круг : 3")
tip=str(input("Введите индекс фигуры : "))
def tr(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
def pr(a,b):
    s = a * b
    return s
def kr(r):
    s = math.pi * (r ** 2)
    return s
if (tip=="2"):
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    print(tr(a, b, c))
elif(tip == "1"):
    a = float(input("a: "))
    b = float(input("b: "))
    print(pr(a, b))
else:
    r = float(input("r: "))
    print(kr(r))



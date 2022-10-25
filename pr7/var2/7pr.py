import math
def ps(a):
    S = (3 * math.sqrt(3) * a ** 2 )/ 2
    return S
a=int(input("Введите длинну ребра правильного шестиугольника : "))
print (ps(a))
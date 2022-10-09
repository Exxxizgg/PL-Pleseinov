a,b,c=[int(x) for x in input("Введите целые числа через пробел").split()],[],[]
for x in a:
    if (x>0):
        b.append(x)
    else:
        c.append(x)
print("Положительные числа : ",*b); print("Отрицательные числа",*c)
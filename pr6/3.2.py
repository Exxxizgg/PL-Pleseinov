from random import *
D = [randint(-10000, 1000) for i in range(8)]
print("Массив изначальный: ",D);
for i in range(8):
    if(D[i]<15):
        D[i]=2*D[i]
    else:
        D[i]=D[i]
print("Массив преобразованный : ",D)
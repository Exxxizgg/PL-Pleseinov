import random
from random import randint
k=int(input("Введите кол-во элементов массива"))
def suma(a):
    s=sum(a)
    return(s)
def sr(a):
    sred=(sum(a))/k
    return(sred)
for i in range (3):
    a = [randint(0,1000) for x in range(k)]
    print("Ваш массив :",a)
    print("Среднеарифметическое",sr(a))
    print("Сумма элементов",suma(a))



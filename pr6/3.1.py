from random import randint
n=int(input("Введите кол-во элементов "))
D = [randint(-10000, 1000) for i in range(n)]
print("Элементы списка(массива): ", D,"\n","Сумма элементов с нечетными индексами : ",sum(x for i, x in enumerate(D) if i % 2 == 1))

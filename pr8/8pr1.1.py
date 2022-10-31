from random import randint
kol=0
sum=0
n=int(input())
a=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=randint(-10,10)
    print()
for i in range(n):
    for j in range(n):
        print("[",a[i][j],end="]")
    print()
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] <= 0:
            continue
        if a[i][j] > 0:
            kol += 1
            sum+= a[i][j]
print("Сумма: ", sum)
print("Кол-во положительных элементов", kol)
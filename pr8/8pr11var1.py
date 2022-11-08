from random import randint
n=int(input())
a=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=randint(-10,10)
    print()
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
m=100
k=0
for i in range(n):
    for j in range(n):
        if a[i][j]<m:
            m=a[i][j]
            k=i
            c=0
print('Cумма элементов строки,имеющей наименьший элемент : ')
for j in range(n):
    c+=a[k][j]
print(c)
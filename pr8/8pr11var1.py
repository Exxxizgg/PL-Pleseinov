P=int(input('Введите порядок матрицы: '))
A=[[int(input()) for j in range(P)] for i in range(P)]
print('Итоговая матрица: ')
for i in range(P):
    for j in range(P):
        print(A[i][j],end=" ")
print()
m=10**10
k=0
for i in range(P):
    for j in range(P):
        if A[i][j]<m:
            m=A[i][j]
            k=i
            c=0
print('Ответ: ')
for j in range(P):
    c+=A[k][j]
print(c)
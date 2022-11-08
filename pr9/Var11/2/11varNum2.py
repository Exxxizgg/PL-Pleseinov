from random import randint
from operator import mul
from functools import reduce
matrix = []
i = 0
n = 3
f = open("11varNum2.txt","r")
for line in f:
    matrix.append([int(x) for x in line.split()])
print(matrix)

def mprint(matrix):
    for row in matrix:
        for item in row:
            print(f'{item:>3}', end=' ')
        print()
tmatrix = list(zip(*matrix))
ps = [reduce(mul, row) for row in tmatrix]
min_p = min(ps)
idx = ps.index(min_p)

if idx < n - 1:
    tmatrix[idx], tmatrix[idx + 1] = tmatrix[idx + 1], tmatrix[idx]
else:
    tmatrix[idx], tmatrix[idx - 1] = tmatrix[idx - 1], tmatrix[idx]

matrix = list(zip(*tmatrix))
f = open("ЗаписьNum2.txt", "a")
f.write(str(matrix))

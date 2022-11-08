2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
from random import randint
from operator import mul
from functools import reduce


def mprint(matrix):
    for row in matrix:
        for item in row:
            print(f'{item:>3}', end=' ')
        print()


n = int(input('Size: '))

matrix = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]
mprint(matrix)
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
mprint(matrix)
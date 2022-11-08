data = []
i = 0
n = 3
f = open("11varNum1.txt","r")
for line in f:
    data.append([int(x) for x in line.split()])
print(data)
m=100
k=0
for i in range(n):
    for j in range(n):
        if data[i][j]<m:
            m=data[i][j]
            k=i
            c=0
print('Cумма элементов строки,имеющей наименьший элемент : ')
for j in range(n):
    c+=data[k][j]
print(c)
f = open("Запись.txt", "a")
f.write(str(c))


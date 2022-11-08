data = []
i = 0
s = 0
pol = 0
f = open("1.txt","r")
for line in f:
    data.append([int(x) for x in line.split()])
print(data)
f.close()
for i in range(4):
    for j in range(i + 1, 4):
        if data[i][j] <= 0:
            continue
        if data[i][j] > 0:
            pol += 1
            s += data[i][j]
            a = str(s)
            b = str(pol)
f = open("1.txt", "a")
f.write("Sum + elementov = ")
f.write(str(s))
f.write("\n")
f.write("Kol +elementov nad diagonaly= ")
f.write(str(pol))
f.close()


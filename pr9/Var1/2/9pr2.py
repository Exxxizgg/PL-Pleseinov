data=[]
N=3
with open('123.txt') as f:
    for line in f:
        data.append([int(x) for x in line.split()])
print(data)
for i, row in enumerate(data):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
f = open("123.txt", "a")
for im in range(N):
    f.write("\n")
    f.write(str(data[im]))

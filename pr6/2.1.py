N=int(input("Введите кол-во элементов массива"))
x=[int(input("Введите целочисленный элемент массива"))for i in range(N)]
min=0;
for i in range(N):
    if (x[i]<min):
        x[i]=min;
        index = x.index(min)
print("Индекс минимального элемента массива : ",index)

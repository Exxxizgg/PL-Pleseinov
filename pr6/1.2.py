n=int(input("Введите кол-во элементов массива"))
x=[float(input("Введите действительное число"))for i in range(n)]
for i in range (n):
    if (x[i]>= 0) and (x[i]<1):
        x[i]=sum(x)/len(x);
print(x)
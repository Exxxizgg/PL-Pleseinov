N=int(input("Введите кол-во элементов массива"))
x=[int(input("Введите целочисленный элемент массива"))for i in range(N)]
maxelement=max(x);
res = x[::-1]
print ("Элементы массива : ",x,"\n" "Максимальный элемент массива = ",maxelement,"\n" "Массив в обратном порядке :",res)

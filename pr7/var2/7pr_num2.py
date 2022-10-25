def ps(x,y):
    s = x * y
    return s
A=[]
for i in range(3):
    print("Введите стороны",i,"-го прямоугольника : ")
    a = int(input("a : "))
    b = int(input("b : "))
    A.append(ps(a,b))
for i in range(3):
    print("Площадь",i,"-ого прямоугольника {:.2f}".format(A[i]))

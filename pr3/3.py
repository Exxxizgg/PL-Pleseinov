a=int(input("Введите число a:"))
b=int(input("Введите число b:"))
if a < b and b > 4:
    x=a + b
elif a > b:
    x= a - b
else:
    x= a**2
print(x)
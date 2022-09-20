a=int(input("Введите число a:"))
x=int(input("Введите число x:"))
if a > 5 and x == 3:
    y = x + a
elif a == 4 or x < 2:
    y = x * a
else:
    y = x ** a
print(y)

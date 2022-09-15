for num in map(float, input("Введите три числа через пробел: ").split()):
    if num >= 1 and num <= 3:
        print(f"Число {num} принадлежит интервалу (1, 3)")
    else:
        print("нет чисел принадлежащих интервалу")

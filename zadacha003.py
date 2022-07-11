# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

def Max(a, b, c, d, e): # функция которая ищет максимальное среди 5 чисел и показывает его индекс
    maxNumber = a
    maxIndex = 0
    index = 0
    for i in a, b, c, d, e:
        if i > maxNumber:
            maxNumber = i
            maxIndex = index
        index +=1

    print(f'Максимальное число: {maxNumber}')
    print(f'Максимальное число имеет индекс: {maxIndex}')


a = int(input('Введите число №1: '))
b = int(input('Введите число №2: '))
c = int(input('Введите число №3: '))
d = int(input('Введите число №4: '))
e = int(input('Введите число №5: '))

Max(a, b, c, d, e)

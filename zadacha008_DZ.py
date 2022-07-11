# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

#           y
#           ^
#           |
#           |
#    (2)    |    (1)
#           |
# ----------0----------> x
#           |
#    (3)    |    (4)
#           |
#           |


# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def NeedDigit(text):  # Функция, которая принимает на вход целое число (координату точки) =! 0
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            coordinate = input()
            coordinate = int(coordinate)
            if coordinate != 0:
                return coordinate
                needTrue = True
            else:
                print('Ошибка ввода. Координата не должы быть равна 0: ')
        except:
            print('Ошибка ввода. Введите целое число не равное 0: ')


def FindQuarter(X, Y): # Функция, которая определяет номер четверти по 2-ум координатам (X и Y)
    if X > 0 and Y > 0: 
        return 1
    elif X < 0 and Y > 0:
        return 2
    elif X < 0 and Y < 0:
        return 3
    else:
        return 4


X = NeedDigit('Введите координату X: ')
Y = NeedDigit('Введите координату Y: ')
numberOfQuarter = FindQuarter (X, Y)
print(f'Вы введи координаты точки: X={X}, Y={Y}\nЭта точка находится в {numberOfQuarter} четверти!')
# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def GetNumber(text):
    needTrue = 0
    while needTrue == 0:
        x1 = input('Введите число: ')
        try:
            x1 = int(x1)
            needTrue = 1
            return x1
        except:
            print('Надо было ввести целое положительное число')

def GetNumber2(text):

    while needTrue == 0:
        x1 = input('Введите число: ')
        if int(x1):
            needTrue = 1
            return x1
        else:
            print('Надо было ввести целое положительное число')



def PrintNumbers(N):
    if N > 0:
        for i in range(-N, N+1, 1):
            print(i, end=' ')
    else: print('Число меньше нуля')


N1 = GetNumber('Введите целое положительно число')
N2 = GetNumber2('Введите целое положительно число')
PrintNumbers(N1)

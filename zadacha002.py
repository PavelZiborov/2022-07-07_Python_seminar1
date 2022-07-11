# Задачи: 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.        
# *Примеры:*        
# - 5, 25 -> да     
# - 4, 16 -> да     
# - 25, 5 -> да     
# - 8,9 -> нет

def Check (a,b):
    if a**2 == b or b**2 == a:
        print('Одно число является квадратом другого!')
    else:
        print('Одно число НЕ является квадратом другого')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
Check(a,b)
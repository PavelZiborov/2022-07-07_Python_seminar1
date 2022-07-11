# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def needWeekDigit (text): # Функция, которая принимает на вход целое число от 1 до 7
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = int(number)
            if 1 <= number <= 7:
                return number
                needTrue = True
            else:
                print('Ошибка ввода. Введите целое число от 1 до 7: ')
        except:
            print('Ошибка ввода. Введите целое число от 1 до 7: ')


numberOfWeek = needWeekDigit('Введите целое число от 1 до 7: ')


if numberOfWeek == 6 or numberOfWeek == 7:
    print('Да, этот день является выходным!')
else:
    print('Нет, этот день НЕ выходной!')


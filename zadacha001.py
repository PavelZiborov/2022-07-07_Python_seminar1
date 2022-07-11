

def GetNumber(a):
    x = False
    while x == False:
        x1 = input('Введите число: ')
        try:
            x1 = int(x1)
            return x1
            x = True
        except:
            print('Надо было ввести целое число')
    

x1 = GetNumber('Введите число: ')
print(x1)




'''
def Summ (x1, x2): # функция сложения 2 чисел
    z = x1 + x2
    print(f'сумма = {z}')
    return z
Summ (x1,x2)
'''

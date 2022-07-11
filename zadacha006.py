
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

def Kratnost(N):
    if N == 30:
        return False
    elif N % 15 == 0:
        return True
    elif N % 5 == 0 and N % 10 == 0:
        return True
    else:
        return False

N = int(input("Введите число: "))
print(Kratnost(N))

#Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
a = int(input("введите первое число: "))
b = int(input("введите второе число: "))

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
print(f"НОК чисел = {a*b//gcd(a,b)}")






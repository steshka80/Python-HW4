# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N

N=int(input("Введите N: "))
multipliers=[]
i=2
while (i!=N):
    if N % i == 0:
        multipliers.append(i)
        N = N / i
    else: 
        i +=1
multipliers.append(i)
print (multipliers)

# Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
d=(input("Введите точность: "))
result=""
temp_str=str(math.pi)
result=temp_str[:-(len(temp_str)-len(d))]
print(result)

# Вычислить число pi c заданной точностью d
# Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)

import math
from math import pi

n = pi
print('Pi = ', pi)

# 1 вариант
# d = input("Задайте точность вычисления ПИ (например 0.001) -> ")
# d = int(len(d) -2)
# print (f'число Пи, с заданной точностью {d} знака после запятой, равно {round(math.pi, d)}')

# 2 вариант
d = 0.0001
print(f'Заданная точность = {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print(round(pi, count))
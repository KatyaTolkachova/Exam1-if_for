#Задаие 4 из экзамена:
import random
a = int(input('Количество чисел:'))
b = [random.randint(1,20) for i in range(a)]
c = int(input('Цифры:'))
d = 0
print(b)
for m in b:
    for j in str(m):
        j = int(j)
        if j == c:
            d += 1
print(d)

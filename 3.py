import random
i = 0
k = 0
s = 0
m = []
while i <= 7:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    x = int(input('Введите число от 1 до 20:'))
    y = int(input('Введите число от 1 до 20:'))
    if a == x and b == y:
        k += 1
    else:
        s += 1
    i += 1
    if i == 4:
        m.append(a)
        m.append(b)
if k == s:
    print(m)


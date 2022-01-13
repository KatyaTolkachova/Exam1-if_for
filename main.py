# Таблица умножения через цикл while:
a = 1
while a <= 10:
    b = 1
    while b <= 10:
        print(a * b, end=" ")
        b += 1
    print(" ")
    a += 1

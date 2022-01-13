#Задаие 6 из экзамена:
a = input('Введите ')
b = ''
s = 0
k = 0
for i in a:
    if i.islower():  # маленький регистр
        b += i
        if len(b) % 2 == 0:
            s += 1
        elif b != ' ':
            b = ' '
    if i.isupper():  # большой регистр
        b += i
        if len(b) % 2 == 0:
            k += 1
        elif b != ' ':
            b = ' '
print('Маленький регистр:', s)
print('Большой регистр', k)
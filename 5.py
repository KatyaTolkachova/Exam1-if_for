#Задаие 5 из экзамена:
a = input('Введите строку:')
b = ' '
for i in a:
    if i.isdigit():
        b += i
    elif b != ' ':
        print(b)
        b = ' '
if b != ' ':
    print(b)



a = input('Введите текст:')
gl = 0
cgl = 0
x = []
for i in a:
    if i in 'aeuo':
        gl += 1
        x.append(i)
    else:
        cgl += 1
print(gl, cgl)
if gl == cgl:
    print(x)

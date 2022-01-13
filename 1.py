a = int(input('Введите семизначное число:'))
b = str(a)
chetn = 0
nechetn = 0
for i in b:
    i = int(i)
    if i % 2 == 0:
        chetn += 1
    else:
        nechetn += 1
sum = 0
if chetn > nechetn:
    for i in b:
        i = int(i)
        sum += i
else:
    a = b
    sum = int(a[0]) + int(a[2]) + int(a[5])
print(sum)

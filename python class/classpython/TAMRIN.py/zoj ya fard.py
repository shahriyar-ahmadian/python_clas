a = int(input('a: '))
a = str(a)
b = 0
c = 0
if a.count('0') != 0:
    b += a.count('0')
if a.count('2') != 0:
    b += a.count('2')
if a.count('4') != 0:
    b += a.count('4')
if a.count('6') != 0:
    b += a.count('6')
if a.count('8') != 0:
    b += a.count('8')
if a.count('1') != 0:
    c += a.count('1')
if a.count('3') != 0:
    c += a.count('3')
if a.count('5') != 0:
    c += a.count('5')
if a.count('7') != 0:
    c += a.count('7')
if a.count('9') != 0:
    c += a.count('9')
if b > c :
    print('zoj')
elif c>b:
    print('fard')
else:
    print('=')
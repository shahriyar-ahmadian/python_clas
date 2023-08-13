username_a = 'pouria'
password_a = 10291029
username_b = 'shahriyar'
password_b = 3511
username_c = 'ali'
password_c = 1234
username = input('username: ')
password = int(input('password: '))
if username == username_a:
    if password == password_a:
        print('welcom')
    else:
        password = int(input('password: '))
        if password == password_a:
            print('welcom')
        else:
            print('you are not registered')
elif username == username_b:
    if password == password_b:
        print('welcom')
    else:
        password = int(input('password: '))
    if password == password_b:
        print('welcom')
    else:
        print('you are not registered')
elif username == username_c:
    if password == password_c:
        print('welcom')
    else:
        password = int(input('password: '))
    if password == password_c:
        print('welcom')
    else:
        print('you are not registered')
else :
    print('you are not registered')
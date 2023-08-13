import random

a= random.randint(0,100)

while True:
    n = int(input('alan nazaret chie:'))

    if a > n :
        print('boro bala :')
    elif a<n:
        print('bia payin:')
    else:
        print('afarin babajan:')
        break
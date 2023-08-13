print('1. -')
print('2. +')
print('3. ×')
print('4. ÷')
print('5. sin(Degree)')
print('6. cos(Degree)')
print('7. tan(Degree)')
print('8. cot(Degree)')
print('9. √')
print('10.x²')
print('11.x**y')
print('12. |…|')
print('13.Round the number')
print('14.  log x ')
import math
op = input('enter operator:')
#1
if (op == '1') or ( op == '-'):
    a = float(input('a:'))
    b= float(input('b:'))
    answer = a- b
    print('ANSWER IS', answer)
#2
elif (op == '2') or (op == '+'):
    a = float(input('a:'))
    b= float(input('b:'))
    answer = a +b
    print('ANSWER IS', answer)
#3
elif (op == '3')or (op == '*'):
    a =float(input('a:'))
    b= float(input('b:'))
    answer = a*b
    print('ANSWER IS', answer)
#4
elif (op == '4') or (op == '/'):
    a= float(input('a:'))
    b= float(input('b:'))
    answer = a/b if b!=0 else 'no no'
    print('ANSWER IS', answer)
#5
elif (op == '5') or (op == 'sin'):
    a = float(input('a:'))
    a2 = (math.sin(a))
    answer =a2 * (math.pi) / 180
    print('ANSWER IS',answer)
#6
elif (op == '6') or (op == 'cos'):
    a = float(input('a:'))
    a2 = (math.cos(a))
    answer = a2 * (math.pi) / 180
    print('ANSWER IS',answer)
#7
elif (op == '7') or (op == 'tan'):
    a = float(input('a:'))
    a2 = (math.tan(a))
    answer = a2 * (math.pi) / 180
    print('ANSWER IS',answer)
#8
elif (op == '8') or (op == 'cot'):
    a = float(input('a:'))
    a2 = (math.tan(a))
    a3 = 1 / a2
    answer = a3 * (math.pi) / 180
    print('ANSWER IS',answer)
#9
elif (op == '9') or (op == '√'):
    a = float(input('a:'))
    answer = math.sqrt(a)
    print('ANSWER IS',answer)
#10
elif(op == '10') or (op == 'x²'):
    a= float(input('a:'))
    answer = a*a
    print('ANSWER IS', answer)
#11
elif (op == '11') or (op == 'x**y'):
    a= float(input('a:'))
    y= float(input('y: '))
    answer =(math.pow(a,y))
    print('ANSWER IS', answer)
#12
elif (op == '11') or (op == '|…|'):
    a= float(input('a:'))
    if a >= 0:
        print('ANSWER IS',a)
    elif a < 0 :
        a2 = -a
        print('ANSWER IS',a2)
#13
elif (op == '12') or (op == 'Round the number'):
    a= float(input('a:'))
    b= a % 10
    if b >= 5:
        print('ANSWER IS',math.ceil(a))
    else:
        print('ANSWER IS',math.floor(a))
#14
elif (op == '13') or (op == 'log x'):
    x = int(input('x: '))
    y = int(input('The base of the logarithm: '))
    answer = (math.log(x,y))
    print('ANSWER IS',answer)
else:
    print('this operator false')
x = 'hello'

def myFunc():
    global y
    y = 'hi'
    print(y + ' world')

myFunc()

print(y + ' world')
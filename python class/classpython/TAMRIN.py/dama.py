7
8
9
10
11
12
13
	
###### Celsius to Fahrenheit/Fahrenheit to Celsius conversion:(0°C × ۹/۵) + ۳۲ = ۳۲°F 
selection = input("Select one option(1 or 2):\n1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius\n")
degree = int(input("Enter Degree: "))
 
def celFarConversion(degree):
    if selection=="1":
        x = (9/5*degree)+32
        print(f"{degree} Degree/s Celsius is {x} Degrees Fahrenheit")
    else:
        x=5/9*(degree-32)
        print(f"{degree} Degrees Fahrenheit is {x} Degree/s Celsius")
 
celFarConversion(degree)
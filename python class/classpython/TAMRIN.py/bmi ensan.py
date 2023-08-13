g = float(input('g(kg): '))
v = float(input('v(cm): '))
v = v /100 
bmi = g / (v *v)
print(bmi)
if 18.5> bmi:
    print('underweight')
elif 18.5<= bmi <= 24.9:
    print('normal =)')
elif 25 <= bmi <= 29.9:
    print('overweight')
elif 30.0<= bmi <= 34.9:
    print('obese')
elif bmi >= 35:
    print('extremly obese!')
#calculator
import math
a = int(input('enter your first number: '))
b = int(input('enter your second number: '))
add = input('do you want to add the numbers:')
if add =='yes':
    print(a+b)
sub = input('do you want to subtract the numbers:')
if sub == 'yes':
    print(a-b)
mult = input('do you want to multiply the numbers:')
if mult == 'yes':
    print(a*b)
division = input('do you want to divide the numbers:')
while b!=0:
    if division == 'yes':
        print(a/b)
    else:
        print("Error: Division by zero is not allowed.")
Mod = input('do you want to find the remainder of a number')
if Mod == 'yes':
    print(a%b)
sqrt = input('do you want to find the square root of a number:')
if sqrt == 'yes':
    n = int(input('enter the number:'))
    print(math.sqrt(n))
cbrt= input('do you want to find the cube root of a number:')
if cbrt == 'yes':
    n = int(input('enter the number:'))
    print(n**(1/3))
power = input('do you want to raise a number:')
if power == 'yes':
    number = int(input('what is the number you want to raise:'))
    p = input('by what number do you want to raise the number:')
    print(number**p)
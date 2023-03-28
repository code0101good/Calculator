import math

num1 = int(input('Num 1: '))
num2 = int(input('Num 2: '))

operator = input('Operator: ')

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print('Error! Try Again...')
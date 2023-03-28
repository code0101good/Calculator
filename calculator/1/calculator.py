import math

def Operator(num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Error! Try Again...')

operator = input('Operator: ')
result = Operator(6,7)
print(result)
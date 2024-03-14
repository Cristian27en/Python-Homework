def divide_numbers(a, b):
    try:
        result  = a / b
        print('Division result: ', result)
    except ZeroDivisionError:
        print('Error: Cannot divide by 0')

try:
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))
    divide_numbers(num1, num2)
except ValueError:
    print('Error: Please enter valid numbers')

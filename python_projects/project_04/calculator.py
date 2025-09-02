#Calculator
import re


operation_input = input("Enter the operation: ")

numbers = re.findall(r'[0-9]+',operation_input)
operator = re.findall(r'[\+\-\*/]',operation_input)

if len(numbers) == 2 and len(operator) == 1:
    a = int(numbers[0])
    b = int(numbers[1])
    op = operator[0]

    if op =='+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b

    print("Result: ", result)
else:
    print("Invalid operation")

import tkinter as tk
import re

window = tk.Tk() # Create a frame
window.title("My Calculator")
window.geometry("400x400") # Windows Size

principal_frame = tk.Frame()

# Entry
enter_number = tk.Entry(principal_frame)
enter_number.pack(pady=5)

def calculator():
    operation_input = enter_number.get().replace(' ', '')
    match = re.fullmatch(r'(-?\d+)([\+\-\*/])(-?\d+)', operation_input)

    if match:
        a, op, b = match.groups()
        a, b = int(a), int(b)
        try:
            if op == '+':
                result = a+b
            elif op == '-':
                result = a-b
            elif op == '*':
                result = a*b
            elif op =='/':
                result = a/b
            result_label.config(text=f"Result: {result}")
        except ZeroDivisionError:
            result_label.config(text="Error: Division by zero")
    else:
        result_label.config(text="Invalid input! Use format: number operator number")

button_calculator = tk.Button(principal_frame, text="Calculator", command=calculator)
button_calculator.pack(pady=5)

def divisor():
    number = enter_number.get()
    if number.isdigit():
        number = int(number)
        rang = range(2, 111)
        divisors = []

        for num in rang:
            if number % num == 0:
                divisors.append(str(num))

        result_label.config(text="Divisors: " + ", ".join(divisors))

button_divisor = tk.Button(principal_frame, text="Divisor", command=divisor)
button_divisor.pack(pady=5)

def verify_even_odd():
    number = enter_number.get()
    if number.isdigit():
        number = int(number)
        if number % 2 == 0:
            result_label.config(text=f'{number} is even')
        else:
            result_label.config(text=f'{number} is odd')
    else:
        result_label.config(text="Please enter a valid number")

button_even_odd = tk.Button(principal_frame, text="Even or Odd", command=verify_even_odd)
button_even_odd.pack(pady=5)

result_label = tk.Label(principal_frame, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Show the frame center with padx and pady
principal_frame.pack(padx=20, pady=20)

# Bucle
window.mainloop()

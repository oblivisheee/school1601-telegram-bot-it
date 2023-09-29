import os
import re
import time

settings = {
    'delay_calc': 10, 
    'use_clr': True,  
    'exit_delay': 3,  
}

while True:
    print("Expression like: 5 * 8 ")
    print('Write "Quit" to exit.')
    expression = input("Write down your math expression: ").replace(" ", "")

    if expression.lower() == "quit":
        print("Exiting...")
        time.sleep(int(settings["exit_delay"]))
        break

    operators = ['*', '/', '-', '+']
    operator_found = any(operator in expression for operator in operators)

    if not operator_found:
        raise Exception("Invalid expression")

    numbers = [float(num) if '.' in num else int(num) for num in re.findall(r'[-+]?\d*\.\d+|\d+', expression)]

    if len(numbers) < 2:
        raise Exception("Invalid expression: Not enough numbers found.")

    result = None

    if '*' in expression:
        result = numbers[0]
        for num in numbers[1:]:
            result *= num
    elif '/' in expression:
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    elif '-' in expression:
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
    elif '+' in expression:
        result = sum(numbers)

    if settings['use_clr']:
        os.system('clear')

    print("Answer of expression:", result)

    if settings['delay_calc'] is not None:
        time.sleep(int(settings["delay_calc"]))

        if settings['use_clr']:
            os.system('clear')
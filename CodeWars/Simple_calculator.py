# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
"""
def calculator(x, y, op):
    """
    Calculadorab que retorna un resultado según la operación.
    :param x: primeri número.
    :param y: segundo número.
    :param op: Operacion a realizar.
    """
    result = 0
    if (type(x) == int) and (type(y) == int) and (op in {'+', '-', '*', '/'}):
        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        elif op == '/':
            result = x / y
    else:
        return "Unknown value"
    return result

def simple_test():
    resultado = calculator(6, 2, '+')
    print(resultado)
    resultado =calculator(5, 4, '/')
    print(resultado)
    resultado =calculator(6, 'g', '+')
    print(resultado)

simple_test()
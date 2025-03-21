def calculator(x, y, op):
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
""""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""
def add_binary(a: int, b: int) -> str:
    return bin(a + b)[2:]
    # bin(...): convierte un número a binario.
    # [2:]: elimina los primeros dos caracteres "0b" para obtener solo el número binario.

if __name__ == '__main__':
    print(add_binary(1,1))
    print(add_binary(0,1))
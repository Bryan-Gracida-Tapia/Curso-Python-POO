# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.

"""
def repeat_str(repeat, string):
    """
    Función que repite n veces una cadena.
    :param repeat: cantidad de veces a repetir la cadena.
    :param string; cadena a repetir.
    """
    return repeat*string





if __name__ == '__main__':
    texto = repeat_str(4, 'a')
    print(texto)
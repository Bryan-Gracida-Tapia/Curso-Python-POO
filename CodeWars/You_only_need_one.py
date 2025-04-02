# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

a can contain numbers or strings. x can be either.

Return true if the array contains the value, false if not.
"""

def check(seq, elem) -> bool:
    """
    Función que devuelve un valor booleano si un elemento se encuentra en una lista
    :param seq: Secuencia
    :param elem: elemento a encontrar
    """
    return elem in seq

if __name__ == '__main__':
    print(check([66, 101], 66))
    print(check(['t', 'e', 's', 't'], 'e'))
    print(check(["what", "a", "great", "kata"], "kat"))
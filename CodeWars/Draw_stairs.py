# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

"""
def draw_stairs(n):
    """
    Función que retorna una escalera segun el numero recibido.
    :param n: contidad de I
    """
    espacio , texto= ' ',''
    for i in range(n):
        texto += f'{espacio * i}I'
        if i != n-1:
            texto += '\n'
    return texto





if __name__ == '__main__':
    forma = draw_stairs(5)
    print(forma)
# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.

However, there is a bug in the method that needs to be resolved.
"""
def kata_13_december(lst):
    """
    Función regresa una lista con los numeros impares de una lista.
    :param lst: lista de números
    """
    aux = list()# se creo una lista auxiliar para guardar la lista deseada
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            aux.append(lst[i])
    return aux
if __name__ == '__main__':

    resultado = kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7])
    print(resultado)
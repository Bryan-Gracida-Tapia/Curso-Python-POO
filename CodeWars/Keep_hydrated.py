# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
"""
def litres(time):
    """
    Función que retorna la catidad de litros de agua que se deben tomar según el tiempo recorrido (1 litro cada hora).
    :param time: Tiempo recorrido.
    """
    return time // 2





if __name__ == '__main__':
    result = litres(0)
    print(result)
    result = litres(4)
    print(result)
    result = litres(5)
    print(result)
    result = litres(12)
    print(result)
    result = litres(1.4)
    print(result)
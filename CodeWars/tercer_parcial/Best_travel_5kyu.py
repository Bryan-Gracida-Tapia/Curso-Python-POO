""""
# Función que dado un límite t, un número k y una lista ls de distancias,
# encuentra la suma máxima de k distancias sin superar t,
# o devuelve None si no existe ninguna combinación válida.

from itertools import combinations

def choose_best_sum(t: int, k: int, ls: list[int]) -> int | None:
    # Generar todas las combinaciones posibles de k distancias
    combos = combinations(ls, k)
    best = None

    for c in combos:
        s = sum(c)
        if s <= t and (best is None or s > best):
            best = s

    return best

# Ejemplos de prueba
ts = [50, 55, 56, 57, 58]
print(choose_best_sum(163, 3, ts))  # 163

xs = [50]
print(choose_best_sum(163, 3, xs))  # None

ys = [91, 74, 73, 85, 73, 81, 87]
print(choose_best_sum(230, 3, ys))  # 228
"""
from itertools import combinations


def choose_best_sum(t: int, k: int, ls: list[int]) -> int | None:
    # Generar todas las combinaciones posibles de k distancias
    combos = combinations(ls, k)
    best = None

    for c in combos:
        s = sum(c)
        if s <= t and (best is None or s > best):
            best = s

    return best

if __name__ == '__main__':
    ts = [50, 55, 56, 57, 58]
    print(choose_best_sum(163, 3, ts))  # 163

    xs = [50]
    print(choose_best_sum(163, 3, xs))  # None

    ys = [91, 74, 73, 85, 73, 81, 87]
    print(choose_best_sum(230, 3, ys))  # 228
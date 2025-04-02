# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return if you're better, else !truefalse
"""
def better_than_average(class_points, your_points):
    """
    Función que según identifica si la puntuación de un estudiante es mayor al promedio de la clase.
    :param class_points: lista con la puntuación de todos los alumnos
    :param your_points: Puntuación a comparar con el promedio
    """
    suma = 0
    for i in class_points : suma +=i
    return your_points > (suma / len(class_points))





if __name__ == '__main__':
    resultado= better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)
    print(resultado)
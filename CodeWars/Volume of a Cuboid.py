# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
Bob needs a fast way to calculate the volume of a rectangular cuboid with three values: the length, width and height of the cuboid.

Write a function to help Bob with this calculation.
"""
def get_volume_of_cuboid(length, width, height):
    """
    Función que encuenta el volumen de un cubo rectángulo.
    :param length: parámetro del cubo
    :param width: parámetro del cubo
    :param height: parámetro del cubo
    """
    return length*width*height





if __name__ == '__main__':
    resultado= get_volume_of_cuboid(1, 2, 2)
    print(resultado)
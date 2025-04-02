# Gracida Tapia Bryan.
# 1 de Abril del 2025.
"""
Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
"""
def people_with_age_drink(age):
    """
    Función que identifica la bebida a tomar según la edad.
    :param age: Eda de la persona.
    """
    if type(age) == int:
        if (age < 14): return 'drink toddy'
        elif (age >= 14 and age < 18): return 'drink coke'
        elif (age >= 18 and age < 21): return 'drink beer'
        elif (age >= 21): return 'drink whisky'
    else:
        return 'unknown value'




if __name__ == '__main__':

    imprimir =people_with_age_drink(13)
    print(imprimir)
    imprimir = people_with_age_drink(0)
    print(imprimir)
    imprimir = people_with_age_drink('f')
    print(imprimir)
    imprimir = people_with_age_drink(17)
    print(imprimir)
    imprimir = people_with_age_drink(25)
    print(imprimir)
    imprimir = people_with_age_drink(21)
    print(imprimir)
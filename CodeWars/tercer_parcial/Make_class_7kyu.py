""""
I don't like writing classes like this:

class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color
Give me the power to create a similar class like this:

Animal = make_class("name", "species", "age", "health", "weight", "color")
"""


# Función make_class que recibe una cantidad variable de nombres de atributos (*attrs)
def make_class(*attrs):
    # Definimos una clase interna llamada DynamicClass
    class DynamicClass:
        # Constructor que recibe valores para cada atributo
        def __init__(self, *values):
            # Validamos que la cantidad de valores coincida con la cantidad de atributos
            if len(values) != len(attrs):
                raise ValueError(f"Expected {len(attrs)} values, got {len(values)}")
            # Asignamos cada valor recibido al atributo correspondiente en el objeto
            for attr, val in zip(attrs, values):
                setattr(self, attr, val)

        # Méodo para representar el objeto como string
        def __repr__(self):
            # Construimos una cadena con el formato "attr=valor" para cada atributo
            attr_str = ', '.join(f"{attr}={getattr(self, attr)!r}" for attr in attrs)
            # Devolvemos el nombre de la clase y los atributos con sus valores
            return f"{self.__class__.__name__}({attr_str})"

    # Retornamos la clase recién definida
    return DynamicClass

if __name__ == '__main__':
    # Creamos la clase Animal con los atributos especificados
    Animal = make_class("name", "species", "age", "health", "weight", "color")

    # Creamos una instancia de Animal pasando los valores para cada atributo en orden
    dog = Animal("Fido", "Dog", 5, "Good", 30, "Brown")

    # Imprimimos la instancia para ver su representación amigable
    print(dog)  # Salida: DynamicClass(name='Fido', species='Dog', age=5, health='Good', weight=30, color='Brown')
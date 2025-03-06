# ///////////////////////////////////////////////////////////////////////////////////////// Estudiante.
class Estudiante:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_tema(self,tema:str) -> None :
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

# ///////////////////////////////////////////////////////////////////////////////////////// Profesor.
class Profesor:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.temas_dominados = []

    def dominar_tema(self,tema:str):
        self.temas_dominados.append(tema)
        print(f"El Pr.{self.nombre} dominó el tema: {tema}")

    def ensenar_tema(self, no_tema: int) -> str:
        contador = 1
        if not self.temas_dominados:
            tema ="No hay temas donimados."
            return tema
        self.temas_dominados.sort()
        print("Lista de temas:")
        for tema in self.temas_dominados:
            print(f"{contador}) {tema}")
            contador += 1
        opcion = input("Selecciona una opción: ")
        while not opcion.isnumeric() or int(opcion) not in range(1,2):
            print("Opción no válida. Intenta de nuevo")
            opcion = input("Selecciona una opción: ")

        return self.temas_dominados[opcion]



# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
if __name__ == '__main__':
    bryan = Estudiante("Bryan")
    bryan.aprender_tema("Python")
    print()
    alberto = Profesor("Alberto")
    alberto.dominar_tema("Clases y objetos")
    alberto.dominar_tema("Estructura de datos")
    tema = alberto.ensenar_tema(2)
    print(f"Se enseñara el tema {tema}")
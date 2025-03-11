# ///////////////////////////////////////////////////////////////////////////////////////// Estudiante.
class Estudiante:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.temas_aprendidos = []

    def __str__(self) -> str :
        return f"Estudiante(nombre:{self.nombre},temas_aprendidos:{self.temas_aprendidos})"

    def aprender_tema(self,tema:str) -> None :
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

# ///////////////////////////////////////////////////////////////////////////////////////// Profesor.
class Profesor:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.temas_dominados = []

    def __str__(self) -> str:
        return f"Profesor(nombre:{self.nombre},temas_dominados:{self.temas_dominados})"

    def dominar_tema(self,tema:str):
        self.temas_dominados.append(tema)
        print(f"El Pr.{self.nombre} dominó el tema: {tema}")

    def ensenar_tema(self, no_tema: int) -> str:

         return self.temas_dominados[no_tema]


    def indice(self,lista:list[str]) -> int:
        contador = 1
        if not lista:
            print("No hay temas donimados.")
            return 0
        lista.sort()
        print("Lista de temas:")
        for tem in lista:
            print(f"{contador}) {tem}")
            contador += 1
        opcion = input("Selecciona una opción: ")

        while not opcion.isnumeric() or int(opcion) not in range(0, contador-1):
            print("Opción no válida. Intenta de nuevo")
            opcion = int(input("Selecciona una opción: "))
        opcion = (int(opcion)) - 1
        return opcion

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
if __name__ == '__main__':
    bryan = Estudiante("Bryan")
    lourdes = Estudiante("Lourdes")
    bryan.aprender_tema("Clases y objetos")
    lourdes.aprender_tema("El internet de las cosas")
    print(bryan)
    print()
    alberto = Profesor("Alberto",)
    alberto.dominar_tema("Clases y objetos")
    alberto.dominar_tema("Estructura de datos")
    alberto.dominar_tema("Variables")
    alberto.dominar_tema("Ciclos")
    print(alberto)

    tema = alberto.indice(alberto.temas_dominados)
    tema_ensenar = alberto.ensenar_tema(tema)
    print(f"Se enseñara el tema {tema}")
    bryan.aprender_tema(tema_ensenar)
    lourdes.aprender_tema(tema_ensenar)
    lourdes.aprender_tema(alberto.ensenar_tema(3))
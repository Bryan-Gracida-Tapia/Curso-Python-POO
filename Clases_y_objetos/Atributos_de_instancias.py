# ///////////////////////////////////////////////////////////////////////////////////////// Estudiante.
class Estudiante:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_tema(self,tema:str):
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

# ///////////////////////////////////////////////////////////////////////////////////////// Profesor.
class Profesor:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.temas_dominados = []

    def dominar_tema(self,tema:str):
        print()

    def ensenar_tema(self, no_tema: int):
        print()

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
if __name__ == '__main__':
    bryan = Estudiante("Bryan")
    bryan.aprender_tema("Python")
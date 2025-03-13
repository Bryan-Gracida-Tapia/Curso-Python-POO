

# ///////////////////////////////////////////////////////////////////////////////////////// Estudiante.
class Avatar:
    no_id = 1
    def __init__(self):
        self.id = Avatar.no_id
        self.x = 0
        self.y = 0
        Avatar.no_id += 1
    def __str__(self) -> str:
        return f"Avatar (ID:{self.id}, posición:{self.y},{self.x})"
    def posicion_actual(self) -> None:
        print(f"Avatar numero {self.id} se encuentra en la posición: ({self.x},{self.y})")

    def Movimiento(self,ordenes:str) -> None:
        for letra in ordenes:
            if letra == "W" or letra == "w" and self.y < 10:
                    self.y += 1
            elif letra == "S" or letra == "s" and self.y > 0:
                    self.y -= 1
            elif letra == "D" or letra == "d" and self.x < 10:
                    self.x += 1
            elif letra == "A" or letra == "a" and self.y > 0:
                    self.x -= 1


# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
if __name__ == '__main__':
    dinosaurio = Avatar()
    ordenes = ""
    while ordenes != "t":
        ordenes = str(input("Ingresa las ordenes de movimiento: "))
        dinosaurio.Movimiento(ordenes)
        dinosaurio.posicion_actual()
        dinosaurio.__str__()

        for letra in ordenes:
            if letra == "T" or letra == "t":
                ordenes = "t"




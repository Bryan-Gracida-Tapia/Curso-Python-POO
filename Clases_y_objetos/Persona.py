class Humano:
    def __init__(self,nombre:str,edad:int,altura:float,peso:float):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def camina(self) -> None :
                print("Estoy caminando")
    def comera(self) -> None :
                print("Estoy comiendo")
    def jugara(self) -> None :
                print("Estoy jugando")
    def dormira(self) -> None :
                print("Estoy durmiendo")

if __name__=="main":
    bryan = Humano("Bryan",21,1.65,65)
    print(bryan.nombre)
    print(bryan.edad)
    print(bryan.altura)
    print(bryan.peso)
    bryan.edad=32
    print(bryan.peso)

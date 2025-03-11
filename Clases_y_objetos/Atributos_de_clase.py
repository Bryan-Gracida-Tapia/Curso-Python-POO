# ///////////////////////////////////////////////////////////////////////////////////////// Empleado.
class Empleado:
    no_id = 1
    def __init__(self,nombre:str,sueldo:float):
        self.nombre = nombre
        self.sueldo = sueldo
        self.id = Empleado.no_id
        Empleado.no_id += 1

    def __str__(self) -> str:
        return f"Empleado (nombre:{self.nombre}, sueldo del empleado:{self.sueldo})"

    def aumentar_sueldo(self,porcentaje:float) -> None:
        aumento = (self.sueldo * porcentaje)/100
        self.sueldo += aumento
        print(f"El empleado {self.nombre} recibio un aumento de: {aumento}")

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
if __name__ == '__main__':
    print(Empleado.no_id)
    juan = Empleado("Juan",3200)
    juan.aumentar_sueldo(35)
    print(juan)

    print()
    print(Empleado.no_id)
    jesus = Empleado("Jesus", 3200)
    jesus.aumentar_sueldo(10)
    print(jesus)

    print()
    print(Empleado.no_id)
    bryan = Empleado("Bryan", 3200)
    bryan.aumentar_sueldo(50)
    print(bryan)


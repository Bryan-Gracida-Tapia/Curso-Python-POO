
# ///////////////////////////////////////////////////////////////////////////////////////// Empleado.
class Empleado:
    """
    Clase que representa a un empleado.
    Atributos : nombre y sueldo.
    Métodos : aumentar_sueldo().
    """
    no_id = 1
    def __init__(self,nombre:str,sueldo:float):
        """
        Constructor de la clase.
        :param nombre: Nombre del empleado.
        :param sueldo: Cantidad que recibe el empleado.
        """
        self.nombre = nombre
        self.sueldo = sueldo
        self.id = Empleado.no_id
        Empleado.no_id += 1

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los atributos del empleado
        """
        return f"Empleado (ID:{self.id}, nombre:{self.nombre}, sueldo del empleado:{self.sueldo})"

    def aumentar_sueldo(self,porcentaje:float) -> None:
        """
        Función para aumentar el sueldo del empleado.
        :param porcentaje: porcentaje que se aumentara a la empresa.
        """
        aumento = (self.sueldo * porcentaje)/100
        self.sueldo += aumento
        print(f"El empleado {self.nombre} recibio un aumento de: {aumento}")
# ///////////////////////////////////////////////////////////////////////////////////////// Empleado.
class Empresa:
    """
    Clase que representa a una empresa.
    Atributos : nombre y lista de empleados.
    Métodos : agregar_empleados(), remover_empleados(),aumentar_sueldo_empleados(), mostrar_empleados().
    """
    def __init__(self, nombre: str, *empleados: Empleado):
        """
        Constructor de la clase.
        :param nombre: Nombre de la empresa.
        :param empleados: Los empleados que forman parte de la empresa.
        """
        self.nombre = nombre
        self.empleados = list(empleados)

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"


    def agregar_empleados(self, *empleados_nuevos: Empleado) -> None:
        """
        Función para añadir empleados a la empresa.
        :param empleados_nuevos: Empleados que se van añadir a la empresa.
        """
        for empleado in empleados_nuevos:
            self.empleados.append(empleado)


    def remover_empleados(self, *empleados_a_eliminar: Empleado) -> None:
        """
        Se utiliza para eliminar a un empleado.
        :param empleados_a_eliminar: Nombres de los empleados a eliminar.
        """
        for empleado in empleados_a_eliminar:
            if empleado in self.empleados:
                print(f"Se despidió el empleado {empleado.nombre} correctamente.")
                self.empleados.remove(empleado)
            else:
                print(f"El empleado {empleado.nombre} no existe dentro de la empresa.")


    def aumentar_sueldo_empleados(self, porcentaje: float) -> None:
        """
        Se utiliza para aumentar el sueldo a todos los empleados.
        :param porcentaje: Recibe el aumento en forma de porcentaje.
        """
        for empleado in self.empleados:
            empleado.sueldo += (empleado.sueldo*porcentaje)/100


    def mostrar_empleados(self) -> None:
        """
        Se utiliza para mostrar los empleados de la empresa.
        """
        print(f"ID    Empleados   Sueldo")

        for empleado in self.empleados:
            print(empleado.id,'   ',empleado.nombre,'   ',empleado.sueldo)


# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
if __name__ == '__main__':
    raul = Empleado('Raul',1200)
    print(raul)
    bryan = Empleado('Bryan',1500)
    print(bryan)
    yamm = Empleado('Yamm', 1500)
    print(yamm)
    jesus = Empleado('Jesus', 1000)
    print(jesus)
    print('\n' * 2)
    roca = Empresa('LA ROCA',raul)
    roca.agregar_empleados(bryan,yamm)
    roca.aumentar_sueldo_empleados(50)
    roca.mostrar_empleados()
    print()
    roca.remover_empleados(raul,jesus)
    print('\n' * 2)
    roca.mostrar_empleados()


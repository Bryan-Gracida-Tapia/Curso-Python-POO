


# ///////////////////////////////////////////////////////////////////////////////////////// Empleado.
class Cuenta_bancaria:
    """
    Clase que representa a un empleado.
    Atributos : nombre y sueldo.
    Métodos : depositar(),retirar(),consultar saldo().
    """
    no_id = 1
    def __init__(self,nombre:str,saldo:float=0):
        """
        Constructor de la clase.
        :param nombre: Nombre del empleado.
        :param saldo: Cantidad que recibe el empleado.
        """
        self.titular = nombre
        self._saldo = saldo
        self.id = Cuenta_bancaria.no_id
        Cuenta_bancaria.no_id += 1

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los atributos del empleado
        """
        return f"Cuenta Bancaria (ID:{self.id}, nombre:{self.titular}, saldo de la cuenta:{self._saldo})"

    def depositar(self,deposito:float) -> None:
        """
        Función para aumentar el sueldo del empleado.
        :param deposito: porcentaje que se aumentara a la empresa.
        """
        self._saldo += deposito
        print(f"Se realizo el deposito de: {deposito} con exito")

    def retirar(self,retiro:float) -> None:
        """
        Función para aumentar el sueldo del empleado.
        :param retiro: porcentaje que se aumentara a la empresa.
        """
        self._saldo -= retiro
        print(f"Se realizo el retiro: {retiro} con exito")

    @property
    def saldo(self)->float:
        return self._saldo
    @saldo.setter
    def saldo(self,nuevo_saldo:float) -> None:
        self._saldo=nuevo_saldo


if __name__ == '__main__':
    cuenta_guadalupe = Cuenta_bancaria('Guadalupe')
    cuenta_guadalupe.__str__()
    print(cuenta_guadalupe)
    cuenta_guadalupe.retirar(50.5)
    print(cuenta_guadalupe)
    cuenta_guadalupe.saldo=5

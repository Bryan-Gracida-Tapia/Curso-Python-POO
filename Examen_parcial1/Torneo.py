# Gracida Tapia Bryan.
# 25 de Marzo del 2025.

from Equipo import Equipo
from colorama import Fore


# ///////////////////////////////////////////////////////////////////////////////////////// Clase Torneo.
class Torneo:
    """
    Clase que representa un torneo de equipos.

    Atributos:
        - nombre_torneo (str): Nombre del torneo.
        - equipos (list[Equipo]): Lista de equipos en el torneo.

    Métodos:
        - agregar_equipos(): Agrega equipos al torneo.
        - eliminar_equipos(): Elimina equipos del torneo.
        - mostrar_equipos(): Muestra los equipos registrados.
    """

    def __init__(self, nombre_torneo: str = "Campeonato Riñas", *equipos: Equipo):
        """
        Constructor de la clase Torneo.

        :param nombre_torneo: Nombre del torneo. (Por defecto: "Campeonato Riñas")
        :param equipos: Equipos que participarán en el torneo.
        """
        self._nombre_torneo = nombre_torneo
        self._equipos = list(equipos)  # Convertimos los argumentos en una lista de equipos

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del torneo.
        """
        return f"Torneo: {self._nombre_torneo} | Equipos participantes: {[equipo.nombre for equipo in self._equipos]}"

    def agregar_equipos(self, *equipos_nuevos: Equipo) -> None:
        """
        Agrega uno o más equipos al torneo.

        :param equipos_nuevos: Equipos a agregar.
        """
        for equipo in equipos_nuevos:
            #if isinstance(equipo, Equipo):  # Asegúrate de que el equipo sea un objeto de la clase Equipo
            self._equipos.append(equipo)
            print(f"Se agrego el equipo: {equipo.nombre} correctamente")
            #else:
                #print(Fore.RED + f"Error: {equipo} no es un equipo válido")

    def eliminar_equipos(self, *equipos_a_eliminar: Equipo) -> None:
        """
        Elimina uno o más equipos del torneo.

        :param equipos_a_eliminar: Equipos a eliminar.
        """
        for equipo in equipos_a_eliminar:
            if equipo in self._equipos:
                self._equipos.remove(equipo)
                print(Fore.RED + f" Se eliminó el equipo: {equipo} correctamente.")
            else:
                print(Fore.YELLOW + f" El equipo {equipo} no está en el torneo.")

    def mostrar_equipos(self) -> None:
        """
        Muestra la lista de equipos participantes en el torneo.
        """
        if not self._equipos:
            print(Fore.RED + " No hay equipos registrados en el torneo.")
            return

        print(Fore.CYAN + f" Equipos en el torneo '{self._nombre_torneo}':")
        i = 1
        for equip in self._equipos:
            # Verificar que 'equip' es una instancia de la clase Equipo
            if isinstance(equip, Equipo):
                print(Fore.WHITE + f"  [{i}]. {equip.nombre}")
            else:
                print(Fore.RED + f"  [{i}]. Error: Elemento no es un equipo válido")
            i += 1
        print(Fore.RESET)  # Restablecer color

    # /////////////////////////////////////////////////////////////////////////////////////// Property.
    @property
    def nombre(self) -> str:
        """ Devuelve el nombre del torneo. """
        return self._nombre_torneo

    @nombre.setter
    def nombre(self, value: str) -> None:
        """ Modifica el nombre del torneo. """
        self._nombre_torneo = value

    @property
    def equipos(self) -> list[Equipo]:
        """ Devuelve una copia de la lista de equipos para evitar modificaciones externas no controladas. """
        return self._equipos[:]


if __name__ == '__main__':
    rinos = Equipo('Eq')
    ti = Equipo('ti')
    ha = Torneo("ha")
    lista = []
    lista.append(rinos)
    lista.append(ti)
    ha.agregar_equipos(*lista)
    print(ha)

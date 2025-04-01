# Gracida Tapia Bryan.
# 25 de Marzo del 2025.
from Jugador import Jugador
from colorama import Fore
# ///////////////////////////////////////////////////////////////////////////////////////// Clase Equipos.
class Equipo:
    """
    Clase que representa un equipo de jugadores.

    Atributos:
        - nombre_equipo (str): Nombre del equipo.
        - jugadores (list[Jugador]): Lista de jugadores en el equipo.
        - id_del_equipo (int): Identificador único del equipo.

    Métodos:
        - agregar_jugadores(): Agrega jugadores al equipo.
        - eliminar_jugadores(): Elimina jugadores del equipo.
        - mostrar_jugadores(): Muestra los jugadores del equipo.
    """

    no_id = 1  # Contador global para asignar IDs únicos

    def __init__(self, nombre_equipo: str = "Nombre pendiente", *jugadores: Jugador ):
        """
        Constructor de la clase Equipo.

        :param nombre_equipo: Nombre del equipo. (Por defecto: "Nombre pendiente")
        :param jugadores: Lista de jugadores iniciales del equipo.
        """
        self._nombre_equipo = nombre_equipo
        self._jugadores = list(jugadores)  # Convertimos en lista
        self._id_del_equipo = Equipo.no_id  # Asigna ID único
        Equipo.no_id += 1  # Incrementa el contador para el siguiente equipo

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del equipo.
        """
        jugadores_nombres = [jugador.nombre for jugador in self._jugadores]
        return f"Equipo: {self._nombre_equipo} | ID: {self._id_del_equipo} | Integrantes: {jugadores_nombres}"

    def agregar_jugadores(self, *jugadores_nuevos: Jugador) -> None:
        """
        Agrega uno o más jugadores al equipo.

        :param jugadores_nuevos: Jugadores a agregar.
        """
        for jugador in jugadores_nuevos:
            if jugador not in self._jugadores:
                self._jugadores.append(jugador)
                print(Fore.GREEN + f"✔ Se agregó el jugador: {jugador.nombre} correctamente.")
            else:
                print(Fore.YELLOW + f"⚠ El jugador {jugador.nombre} ya está en el equipo.")

    def eliminar_jugadores(self, *jugadores_a_eliminar: Jugador) -> None:
        """
        Elimina uno o más jugadores del equipo.

        :param jugadores_a_eliminar: Jugadores a eliminar.
        """
        for jugador in jugadores_a_eliminar:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)
                print(Fore.RED + f" Se eliminó al jugador: {jugador.nombre} correctamente.")
            else:
                print(Fore.YELLOW + f" El jugador {jugador.nombre} no está en el equipo.")

    def mostrar_jugadores(self) -> None:
        """
        Muestra la lista de jugadores del equipo.
        """
        if not self._jugadores:
            print(Fore.RED + " No hay jugadores en este equipo.")
            return

        print(Fore.CYAN + f" Jugadores en el equipo '{self._nombre_equipo}':")
        for i, jugador in enumerate(self._jugadores, start=1):
            print(Fore.WHITE + f"  [{i}]. {jugador.nombre}")
        print(Fore.RESET)  # Restablecer color

    # /////////////////////////////////////////////////////////////////////////////////////// Property.
    @property
    def nombre(self) -> str:
        """ Devuelve el nombre del equipo. """
        return self._nombre_equipo

    @nombre.setter
    def nombre(self, value: str) -> None:
        """ Modifica el nombre del equipo. """
        self._nombre_equipo = value

    @property
    def integrantes(self) -> list[Jugador]:
        """ Devuelve una copia de la lista de jugadores para evitar modificaciones externas no controladas. """
        return self._jugadores[:]

    @integrantes.setter
    def integrantes(self, value: list[Jugador]) -> None:
        """ Modifica la lista de jugadores del equipo. """
        self._jugadores = list(value)

    @property
    def id(self) -> int:
        """ Devuelve el identificador único del equipo. """
        return self._id_del_equipo

if __name__ == '__main__':
    moscos = Equipo("Moscos",)
    print(moscos)
    print(moscos.mostrar_jugadores())
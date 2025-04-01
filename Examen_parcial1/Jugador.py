# Gracida Tapia Bryan.
# 25 de Marzo del 2025.

# ///////////////////////////////////////////////////////////////////////////////////////// Clase Equipos.
class Jugador:
    """
    Clase que representa un jugador de fútbol.

    Atributos:
        - nombre (str): Nombre del jugador.
        - numero_camiseta (int): Número de camiseta del jugador.
        - cantidad_goles (int): Cantidad de goles anotados.

    Métodos:
        - anotar_goles(): Suma goles al jugador.
    """

    def __init__(self, nombre_jugador: str = "Nombre pendiente", numero_camiseta: int = 100, cantidad_goles: int = 0):
        """
        Constructor de la clase Jugador.

        :param nombre_jugador: Nombre del jugador. (Por defecto: "Nombre pendiente")
        :param numero_camiseta: Número de la camiseta del jugador. (Por defecto: 100)
        :param cantidad_goles: Cantidad inicial de goles. (Por defecto: 0)
        """
        self._nombre_jugador = nombre_jugador
        self._numero_camiseta = max(1, numero_camiseta)  # Asegurar número positivo
        self._cantidad_goles = max(0, cantidad_goles)  # No puede ser negativo

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del jugador.
        """
        return f" Jugador: {self._nombre_jugador} | Camiseta: {self._numero_camiseta} | Goles: {self._cantidad_goles}"

    def anotar_goles(self, goles: int) -> None:
        """
        Agrega goles al jugador.

        :param goles: Cantidad de goles a agregar.
        """
        if goles < 0:
            print("⚠ No puedes restar goles. Usa un valor positivo.")
            return

        self._cantidad_goles += goles
        print(f" {goles} goles añadidos a {self._nombre_jugador}. Total: {self._cantidad_goles} goles.")

    # /////////////////////////////////////////////////////////////////////////////////////// Property.
    @property
    def nombre(self) -> str:
        """ Devuelve el nombre del jugador. """
        return self._nombre_jugador

    @nombre.setter
    def nombre(self, value: str) -> None:
        """ Modifica el nombre del jugador. """
        self._nombre_jugador = value

    @property
    def camiseta(self) -> int:
        """ Devuelve el número de la camiseta del jugador. """
        return self._numero_camiseta

    @camiseta.setter
    def camiseta(self, value: int) -> None:
        """ Modifica el número de la camiseta del jugador. """
        if value > 0:
            self._numero_camiseta = value
        else:
            print("⚠ El número de camiseta debe ser mayor que 0.")

    @property
    def goles(self) -> int:
        """ Devuelve la cantidad de goles anotados. """
        return self._cantidad_goles

    @goles.setter
    def goles(self, value: int) -> None:
        """ Modifica la cantidad de goles. No puede ser negativo. """
        if value >= 0:
            self._cantidad_goles = value
        else:
            print("⚠ La cantidad de goles no puede ser negativa.")

if __name__ == '__main__':
    ryan = Jugador('Ryan',7,30)
    print(ryan)
    print(f"{ryan.nombre} tiene una cantidad de: {ryan.goles} goles ")
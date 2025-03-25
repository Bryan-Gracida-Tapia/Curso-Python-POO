# Gracida Tapia Bryan.
# 25 de Marzo del 2025.

import Ej2_Scoreboard
class Window:
    """
    Clase que representa a la pantalla.
    Atributos : text,width,height,scoreboard.
    Métodos : draw_scoreboard(), update_score().
    """
    def __init__(self,text:str,width:int,height:int,scoreboard:Ej2_Scoreboard.Scoreboard = Ej2_Scoreboard.Scoreboard()):
        """
        Constructor de la clase.
        :param text: Recibe una cadena
        :param width: Recibe un entero
        :param height: Recibe un entero
        :param scoreboard: Recibe una clase que se exporta
        """
        self._title = text
        self._width = width
        self._height = height
        self._scoreboard = scoreboard

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los atributos de la clase
        """
        return f"Window (title:{self._title}, Width:{self._width}, height:{self._height}, Scoreboard:{self._scoreboard})"

    def draw_scoreboard(self) -> None:
        """
        Se utiliza para imprimir en pantalla los puntos
        """
        self._scoreboard.draw()


    def update_score(self,points:int)->None:
        """
        Se utiliza para actualizar los puntos
        """
        self._scoreboard.points=points

    # /////////////////////////////////// Property.

    @property               # /////////////////////////////////// title.
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value:str) -> None:
        self.title = value


    @property  # /////////////////////////////////// width.
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        self._width = value

    @property  # /////////////////////////////////// height.
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._height = value

    @property  # /////////////////////////////////// scoreboard.
    def scoreboard(self) :
        return self._scoreboard

    @scoreboard.setter
    def scoreboard(self, value:Ej2_Scoreboard.Scoreboard) -> None:
         self._scoreboard = value


if __name__ == "__main__":
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Ej2_Scoreboard.Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)


    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")
# Gracida Tapia Bryan.
# 25 de Marzo del 2025.

# ///////////////////////////////////////////////////////////////////////////////////////// Clase Scoreboard.
class Scoreboard:
    """
    Clase que representa a la pantalla.
    Atributos : points,text_color,fond,size.
    Métodos : draw().
    """

    # /////////////////////////////////// Init.
    def __init__(self, points: int =0 , text_color: tuple[int, int , int] = (0,0,0), fond:str ="Kimono", size:float = 48):
        """
        Constructor de la clase.
        :param points: Recibe el numero de puntos iniciales.
        :param text_color: Recibe las cordenadas del color de texto.
        :param fond: Recibe el tipo de letra.
        :param size: Recibe el tamaño de letra.
        """
        self._points = points
        self._text_color = text_color
        self._fond = fond
        self._size = size
        self.x = 0
        self.y = 0

    # /////////////////////////////////// Str.
    def __str__(self) -> str:
        """
        Se utiliza para mostrar los atributos de la clase
        """
        return f"Score (points:{self._points})"

    # /////////////////////////////////// Draw.
    def draw(self) -> None:
        """
        Se utiliza para imprimir los puntos en forma de cadena
        """
        print(f"Score: {self._points}")

    # /////////////////////////////////// Property.
    @property               # /////////////////////////////////// points.
    def points(self) -> int:
        return self._points

    @points.setter
    def points(self, value: int) -> None:
        self._points = value

    @property  # /////////////////////////////////// Text color.
    def text_color(self) -> tuple:
        return self._text_color

    @text_color.setter
    def text_color(self, value: tuple) -> None:
        self.text_color = value

    @property  # /////////////////////////////////// Fond.
    def fond(self) -> str:
        return self._fond

    @fond.setter
    def fond(self, value: str) -> None:
        self.fond = value
    
    @property  # /////////////////////////////////// Size.
    def size(self) -> float:
        return self._size

    @size.setter
    def size(self, value:float) -> None:
         self._size = value

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
if __name__ == "__main__":
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(10, fond="Arial", text_color=(127,127,127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()
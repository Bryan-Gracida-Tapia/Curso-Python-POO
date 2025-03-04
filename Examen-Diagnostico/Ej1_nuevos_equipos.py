# Gracida Tapia Bryan.
# 04 de Marzo del 2025.
# Descripción:
# Programa que genera equipos aleatorios.
from colorama import Fore
import random
# ///////////////////////////////////////////////////////////////////////////////////////// Menu Selección.
def menu():
    """

    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.CYAN + "     *** Menú ***")
    print(Fore.CYAN + "[1].- Generar nuevos equipos")
    print(Fore.RED + "[2].- Salir")
    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 7):
        print(Fore.RED + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.WHITE + "Selecciona una opción: ")
    return int(opcion)
    
def limpiar() -> None :
    """
    Imprime varias lineas en blanco, para simular una pantalla limpia.
    """
    print("\n" * 50)

# ///////////////////////////////////////////////////////////////////////////////////////// Función crear y mostrar el tablero.

def seleccionar_equipos(equipo1,equipo2,equipo3,equipo4) -> None:
    """
    Selecciona integrantes de las listas sin que se repitan para hacer equipos
    :param:recibe las lista con los eqipos existentes
    """
    limpiar()
    i = 0
    while i <= 5:
        integrante_1 = None
        integrante_2 = None
        while integrante_1 == None:
            primera_list = random.randint(1,2)
            if primera_list == 1:
                integrante_1 = random.choice(equipo1)
                equipo1.remove(integrante_1)
            elif primera_list == 2:
                integrante_1 = random.choice(equipo2)
                equipo2.remove(integrante_1)
                
        while integrante_2 == None:
            segunda_list = random.randint(3,4) 
            if segunda_list == 3:
                integrante_2 = random.choice(equipo3)
                equipo3.remove(integrante_2)
            elif segunda_list == 4:
                integrante_2 = random.choice(equipo4)
                equipo4.remove(integrante_2)
        i+=1
        print(f"Equipo {i}: {integrante_1} y {integrante_2}")
    

# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def armar_equipos() -> None:
    """
    Función donde se encuentra las llamadas a la funcion principal
    :return:
    """
    if __name__ == "__main__":

        equipo1 = ["Hector", "Addi", "Jesus alberto"]
        equipo2 = ["Bryan", "Jamileth", "rolinda"]
        equipo3 = ["Juan", "Galilea", "Jennifer"]
        equipo4 = ["Tania", "Patricia", "Rebeca"]
        
        opcion = menu()

        if opcion == 1:
            seleccionar_equipos(equipo1,equipo2,equipo3,equipo4)
        else:
            print(Fore.RED + "Saliendo del programa...")

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nievl de módulo.
armar_equipos()

# Gracida Tapia Bryan.
# 09 de Enero del 2025.
# Descripción:

from colorama import Fore
from Equipo import Equipo
from Torneo import Torneo
from Jugador import Jugador


# ///////////////////////////////////////////////////////////////////////////////////////// limpiar.
def limpiar():
    print("\n" * 3)


# ///////////////////////////////////////////////////////////////////////////////////////// Menú principal.
def menu_principal():
    """
    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.CYAN + "     Bienvenido al generador de torneos")
    print(Fore.CYAN + "[1].- Crear nuevo torneo")
    print(Fore.CYAN + "[2].- Seleccionar torneo")
    print(Fore.RED + "[3].- Salir")

    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 4):
        print(Fore.RED + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.WHITE + "Selecciona una opción: ")
    return int(opcion)


# ///////////////////////////////////////////////////////////////////////////////////////// Menú Selección Operación.
def menu_seleccion_operaciones():
    """
    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.CYAN + "[1].- Crear nuevo jugador")
    print(Fore.CYAN + "[2].- Crear nuevo equipo")
    print(Fore.CYAN + "[3].- Ver lista de jugadores")
    print(Fore.CYAN + "[4].- Ver lista de equipos")
    print(Fore.CYAN + "[5].- Agregar jugadores a un equipo")
    print(Fore.CYAN + "[6].- Eliminar jugadores de un equipo")
    print(Fore.CYAN + "[7].- Agregar equipos al torneo")
    print(Fore.CYAN + "[8].- Eliminar equipos del torneo")
    print(Fore.CYAN + "[9].- Anotar goles a un jugador")
    print(Fore.CYAN + "[10].- Conocer el total de goles de los equipos")
    print(Fore.CYAN + "[11].- Generar rol de juegos")
    print(Fore.RED + "[12].- Salir")

    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 13):
        print(Fore.RED + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.WHITE + "Selecciona una opción: ")
    return int(opcion)


# ///////////////////////////////////////////////////////////////////////////////////////// Menú torneos.
def menu_torneos(torneos: list[Torneo] or list[Equipo] or list[Jugador]):
    """
    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.CYAN + "     Torneos")
    for i, torneo in enumerate(torneos, start=1):
        print(Fore.CYAN + f"[{i}].- {torneo.nombre}")

    print(Fore.RED + f"[{len(torneos) + 1}].- Salir")

    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, len(torneos) + 2):
        print(Fore.RED + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.WHITE + "Selecciona una opción: ")

    return int(opcion) - 1


# ///////////////////////////////////////////////////////////////////////////////////////// Menú equipos.
def menu_equipos(equipos: list[Equipo]):
    """
    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.CYAN + "     Equipos")
    for i, equipo_n in enumerate(equipos, start=1):
        print(Fore.CYAN + f"[{i}].- {equipo_n.nombre}")

    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, len(equipos) + 1):
        print(Fore.RED + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.WHITE + "Selecciona una opción: ")

    return int(opcion) - 1


# ///////////////////////////////////////////////////////////////////////////////////////// Menú jugadores.
def menu_jugadores(integrantes: list[Jugador]):
    """
    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.CYAN + "     Jugadores")
    for i, jugador in enumerate(integrantes, start=1):
        print(Fore.CYAN + f"[{i}].- {jugador.nombre}")

    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, len(integrantes) + 1):
        print(Fore.RED + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.WHITE + "Selecciona una opción: ")

    return int(opcion) - 1

if __name__ == '__main__':
    ryan = Jugador('Ryan',7,10)
    yamm = Jugador('yamm',13,4)
    jesus = Jugador('Chay', 1, 0)
    rinos = Equipo("Rinos",ryan,yamm)
    panchos = Equipo("panchos", jesus, yamm)
    redbull = Torneo("Redbull", rinos,panchos)
    #menu_equipos(redbull.equipos)
    eleccion = menu_seleccion_operaciones()
    if eleccion != 12:
        eleccion = int(menu_equipos(redbull.equipos))
        if eleccion != len(redbull.equipos):
            equipo = redbull.equipos[eleccion]

            integrante = equipo.integrantes[menu_jugadores(equipo.integrantes)]
            print(integrante._nombre_jugador)

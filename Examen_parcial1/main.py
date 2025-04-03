# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# juegos.
import itertools

import Menus
from colorama import Fore
import random
from Equipo import Equipo
from Torneo import Torneo
from Jugador import Jugador


def main()->None:
    opcion = 0
    torneos = []
    equipos_libres = []
    jugadores_libres = []
    Menus.limpiar()
    while opcion != 3:

        print(Fore.RED +    "████████╗░█████╗░██████╗░███╗░░██╗███████╗ ░█████╗╗░██████╗")
        print(Fore.CYAN +   "╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝ ██╔══██╗██╔════╝")
        print(Fore.YELLOW + "░░░██║░░░██║░░██║██████╔╝██╔██╗██║█████╗ ░░██║░░██║╚█████╗░")
        print(Fore.BLUE +   "░░░██║░░░██║░░██║██╔══██╗██║╚████║██╔══╝ ░░██║░░██║░╚═══██╗")
        print(Fore.GREEN +  "░░░██║░░░╚█████╔╝██║░░██║██║░╚███║███████╗ ╚█████╔╝██████╔╝")
        print(Fore.RED +    "░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝ ░╚════╝░╚═════╝░")

        opcion = Menus.menu_principal()

        print()
        if opcion == 1:                     # ................................ Crear torneo.
            nombre = input("Ingrese el nombre del torneo: ")
            torneo = Torneo(nombre)
            torneos.append(torneo)

        elif opcion == 2:                   # ................................ Seleccionar un torneo
            eleccion = Menus.menu_torneos(torneos)
            if eleccion != len(torneos):
                torneo_elejido = torneos[eleccion]
                print(Fore.RED + f"     Bienvenido al torneo: {torneo_elejido.nombre}")
                print(torneo_elejido)
                # ................................ Seleccionar una operación
                operacion = 0
                while operacion != 12:
                    operacion = Menus.menu_seleccion_operaciones()
                    # ................................ Crear jugador nuevo.
                    if operacion == 1:
                        nombre = input(Fore.WHITE + "Nombre del jugador: ")
                        camiseta = int(input(Fore.WHITE + "Número de camiseta: "))
                        nuevo_jugador = Jugador(nombre, camiseta)
                        jugadores_libres.append(nuevo_jugador)
                        print(Fore.GREEN + f"Jugador {nombre} creado correctamente.")
                    # ................................ Crear un equipo nuevo.
                    elif operacion == 2:
                        nombre_equipo = input(Fore.WHITE + "Nombre del equipo: ")
                        jugador_inicial = Jugador('pendiente',0,0)
                        equipo = Equipo(nombre_equipo,jugador_inicial)
                        equipos_libres.append(equipo)
                        print(Fore.GREEN + f"Equipo {nombre_equipo} creado correctamente.")
                    # ................................ Ver lista de jugadores.
                    elif operacion == 3:
                        if not torneo_elejido.equipos:
                            print(Fore.RED + "No hay jugadores creados.")
                        else:
                            for equipo in torneo_elejido.equipos:
                                print(Fore.CYAN + f"     {equipo}")
                                equipo.mostrar_jugadores()
                    # ................................ Ver lista de equipos.
                    elif operacion == 4:
                        if not torneo_elejido.equipos:
                            print(Fore.RED + "No hay equipos creados.")
                        else:
                            torneo_elejido.mostrar_equipos()
                    # ................................ Agregar jugadores a un equipo.
                    elif operacion == 5:
                        seguir = 1
                        if not torneo_elejido.equipos:  # Verificar que hay equipos en el torneo
                            print(Fore.RED + "No hay equipos disponibles en el torneo.")
                        else:
                            equipo_elejido = torneo_elejido.equipos[Menus.menu_equipos(torneo_elejido.equipos)]
                            jugadores_elejidos = []

                            while seguir != 0:
                                if not jugadores_libres:  # Verificar que hay jugadores disponibles
                                    print(Fore.RED + "No hay jugadores disponibles para agregar.")
                                    break

                                try:
                                    jugador = jugadores_libres[Menus.menu_jugadores(jugadores_libres)]
                                except IndexError:
                                    print(Fore.RED + "Selección inválida. Intenta de nuevo.")
                                    continue  # Volver a pedir la selección

                                jugadores_elejidos.append(jugador)
                                print("Seleccionado correctamente.")
                                jugadores_libres.remove(jugador)  # No hay problema en eliminarlo aquí

                                seguir = input("Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                while not seguir.isdigit() or int(seguir) not in [0, 1]:
                                    print(Fore.RED + "Opción no válida. Intenta de nuevo.")
                                    seguir = input(Fore.GREEN + "Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                seguir = int(seguir)

                            if jugadores_elejidos:  # Si hay jugadores seleccionados, agregarlos al equipo
                                equipo_elejido.agregar_jugadores(*jugadores_elejidos)
                            else:
                                print(Fore.YELLOW + "No se agregó ningún jugador al equipo.")
                    # ................................ Eliminar jugadores de un equipo.
                    elif operacion == 6:
                        seguir = 1

                        #  Verificar si hay equipos disponibles en el torneo
                        if not torneo_elejido.equipos:
                            print(Fore.RED + "No hay equipos disponibles en el torneo.")
                        else:
                            try:
                                equipo = torneo_elejido.equipos[
                                    Menus.menu_equipos(torneo_elejido.equipos)]  #  Manejo de índice fuera de rango
                            except IndexError:
                                print(Fore.RED + "Selección de equipo inválida.")
                            else:
                                lista = equipo.integrantes

                                if not lista:  # Verificar si hay jugadores en el equipo
                                    print(Fore.RED + "El equipo no tiene jugadores.")
                                else:
                                    jugadores_elejidos = []

                                    while seguir != 0:
                                        try:
                                            jugador = lista[Menus.menu_jugadores(lista)]  # Manejo de índice fuera de rango
                                        except IndexError:
                                            print(Fore.RED + "Selección de jugador inválida. Intenta de nuevo.")
                                            continue  # Volver a solicitar la selección

                                        jugadores_elejidos.append(jugador)
                                        print(Fore.GREEN + "Jugador seleccionado correctamente.")

                                        seguir = input("Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                        while not seguir.isdigit() or int(seguir) not in [0, 1]:
                                            print(Fore.RED + "Opción no válida. Intenta de nuevo.")
                                            seguir = input(
                                                Fore.WHITE + "Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                        seguir = int(seguir)

                                    # Se eliminan los jugadores después del bucle
                                    for jugador in jugadores_elejidos:
                                        lista.remove(jugador)

                                    # Verificar que haya jugadores antes de eliminarlos
                                    if jugadores_elejidos:
                                        equipo.eliminar_jugadores(*jugadores_elejidos)
                                        print(Fore.GREEN + "Jugadores eliminados exitosamente.")
                                    else:
                                        print(Fore.YELLOW + "No se eliminó ningún jugador del equipo.")
                    # ................................ Agregar equipos al torneo.
                    elif operacion == 7:
                        seguir = 1
                        equipos_elejidos = []

                        if not equipos_libres:  # Verificar si hay equipos disponibles
                            print(Fore.RED + "No hay equipos disponibles para seleccionar.")
                        else:
                            while seguir != 0:
                                if not equipos_libres:  # Verificar que hay jugadores disponibles
                                    print(Fore.RED + "No quedan equipos libres.")
                                    break
                                else:
                                    try:
                                        equipo = equipos_libres[Menus.menu_equipos(equipos_libres)]  # Manejo de errores de índice
                                        print(equipo)
                                    except IndexError:
                                        print(Fore.RED + "Selección inválida. Intenta de nuevo.")
                                        continue  # Volver a solicitar la selección

                                    equipos_elejidos.append(equipo)
                                    print(Fore.GREEN + "Equipo seleccionado correctamente.")
                                    equipos_libres.remove(equipo)

                                    seguir = input("Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                    while not seguir.isdigit() or int(seguir) not in [0, 1]:
                                        print(Fore.RED + "Opción no válida. Intenta de nuevo.")
                                        seguir = input(Fore.WHITE + "Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                    seguir = int(seguir)

                            # Verificar que haya equipos antes de agregarlos al torneo
                            if equipos_elejidos:
                                torneo_elejido.agregar_equipos(*equipos_elejidos)
                                print(Fore.GREEN + "Equipos agregados exitosamente al torneo.")
                            else:
                                print(Fore.YELLOW + "No se agregó ningún equipo al torneo.")
                    # ................................ Eliminar equipos del torneo.
                    elif operacion == 8:
                        seguir = 1
                        lista = torneo_elejido.equipos

                        if not lista:  # Verificar si hay equipos disponibles
                            print(Fore.RED + "No hay equipos disponibles para eliminar.")
                        else:
                            equipos_elejidos = []

                            while seguir != 0:
                                try:
                                    equipo = lista[Menus.menu_equipos(lista)]  # Manejo de índice fuera de rango
                                except IndexError:
                                    print(Fore.RED + "Selección inválida. Intenta de nuevo.")
                                    continue  # Volver a solicitar la selección

                                equipos_elejidos.append(equipo)
                                print(Fore.GREEN + "Equipo seleccionado correctamente.")

                                seguir = input("Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                while not seguir.isdigit() or int(seguir) not in [0, 1]:
                                    print(Fore.RED + "Opción no válida. Intenta de nuevo.")
                                    seguir = input(Fore.WHITE + "Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                seguir = int(seguir)

                            # Se eliminan los equipos después del bucle
                            for equipo in equipos_elejidos:
                                lista.remove(equipo)

                            # Verificar que haya equipos antes de eliminarlos
                            if equipos_elejidos:
                                torneo_elejido.eliminar_equipos(*equipos_elejidos)
                                print(Fore.GREEN + "Equipos eliminados exitosamente del torneo.")
                            else:
                                print(Fore.YELLOW + "No se eliminó ningún equipo del torneo.")
                    # ................................ Anotar goles a un jugador.
                    elif operacion == 9:
                        equipo = torneo_elejido.equipos[Menus.menu_equipos(torneo_elejido.equipos)]
                        jugador = equipo.integrantes[Menus.menu_jugadores(equipo.integrantes)]
                        goles = input(f"ingrese la cantidad de goles que se le anotaran al jugador {jugador}: ")
                        while not goles.isnumeric() :
                            print(Fore.RED + "Opción no válida. Intenta de nuevo")
                            goles = input(Fore.WHITE + "Selecciona una opción: ")
                        goles = int(goles)
                        jugador.anotar_goles(goles)
                    # ................................ Conocer el total de goles de los equipos.
                    elif operacion == 10:
                        for equipo in torneo_elejido.equipos:
                            total_goles = sum(jugador.goles for jugador in equipo.integrantes)
                            print(f"El total de goles del equipo {equipo.nombre} es: {total_goles}")
                    # ................................ Generar rol de juegos.
                    elif operacion == 11:
                        torneo_elejido.generar_rol_juegos()
                    # ................................ Salir del torneo.
                    elif operacion == 12:
                        print(f"Saliendo..")

                    print()
                    print(Fore.WHITE + "-----------------------------")
                    print()
        elif opcion == 3:  # ................................ Salir del programa.
            print("Saliendo del programa...")
        else:
            print("Opcion no valida, intente de nuevo")

        print()
        print(Fore.WHITE + "-----------------------------")
        print()

if __name__ == '__main__':
    main()
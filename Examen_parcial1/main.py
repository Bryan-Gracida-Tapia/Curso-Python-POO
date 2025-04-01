# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# juegos.
import Menus
from colorama import Fore
from Equipo import Equipo
from Torneo import Torneo
from Jugador import Jugador

from colorama import Fore

def main()->None:
    opcion = 0
    torneos = []
    equipos_libres = []
    jugadores_libres = []
    while opcion != 6:
        Menus.limpiar()
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
                print(torneo_elejido)
                # ................................ Seleccionar una operación
                operacion = 0
                while operacion != 12:
                    operacion = Menus.menu_seleccion_operaciones()
                    if operacion == 1:  # ................................ Crear jugador nuevo.
                        nombre = input(Fore.WHITE + "Nombre del jugador: ")
                        camiseta = int(input(Fore.WHITE + "Número de camiseta: "))
                        nuevo_jugador = Jugador(nombre, camiseta)
                        jugadores_libres.append(nuevo_jugador)
                        print(Fore.GREEN + f"Jugador {nombre} creado correctamente.")

                    elif operacion == 2:  # ................................ Crear un equipo nuevo.
                        nombre_equipo = input(Fore.WHITE + "Nombre del equipo: ")
                        jugador_inicial = Jugador('pendiente',0,0)
                        equipo = Equipo(nombre_equipo,jugador_inicial)
                        equipos_libres.append(equipo)
                        print(Fore.GREEN + f"Equipo {nombre_equipo} creado correctamente.")

                    elif operacion == 3:  # ................................ Ver lista de jugadores.
                        if not torneo_elejido.equipos:
                            print(Fore.RED + "No hay jugadores creados.")
                        else:
                            for equipo in torneo_elejido:
                                print(Fore.CYAN + f"     {equipo}")
                                equipo.mostrar_jugadores()

                    elif operacion == 4:  # ................................ Ver lista de equipos.
                        if not torneo_elejido.equipos:
                            print(Fore.RED + "No hay equipos creados.")
                        else:
                            torneo_elejido.mostrar_equipos()

                    elif operacion == 5:  # ................................ Agregar jugadores a un equipo.
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
                                    seguir = input(Fore.WHITE + "Ingrese un 1 para seguir o 0 para terminar: ").strip()
                                seguir = int(seguir)

                            if jugadores_elejidos:  # Si hay jugadores seleccionados, agregarlos al equipo
                                equipo_elejido.agregar_jugadores(*jugadores_elejidos)
                            else:
                                print(Fore.YELLOW + "No se agregó ningún jugador al equipo.")

                    elif operacion == 6:  # ................................ Eliminar jugadores de un equipo.
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

                    elif operacion == 7:  # ................................ Agregar equipos al torneo.
                        seguir = 1
                        equipos_elejidos = []

                        if not equipos_libres:  # Verificar si hay equipos disponibles
                            print(Fore.RED + "No hay equipos disponibles para seleccionar.")
                        else:
                            while seguir != 0:
                                try:
                                    equipo = equipos_libres[Menus.menu_equipos(equipos_libres)]  # Manejo de errores de índice
                                    print(equipo)
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

                            #Se eliminan los equipos seleccionados después del bucle
                            for equipo in equipos_elejidos:
                                equipos_libres.remove(equipo)

                            # Verificar que haya equipos antes de agregarlos al torneo
                            if equipos_elejidos:
                                torneo_elejido.agregar_equipos(*equipos_elejidos)
                                print(Fore.GREEN + "Equipos agregados exitosamente al torneo.")
                            else:
                                print(Fore.YELLOW + "No se agregó ningún equipo al torneo.")

                    elif operacion == 8:  # ................................ Eliminar equipos del torneo.
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

                    elif operacion == 9:  # ................................ Anotar goles a un jugador.
                        equipo = torneo_elejido.equipos[Menus.menu_equipos(torneo_elejido.equipos)]
                        jugador = equipo.integrantes[Menus.menu_jugadores(equipo.integrantes)]
                        goles = int(input("Ingrese la cantidad de goles a anotar: "))
                        jugador.anotar_goles(goles)

                    elif operacion == 10:  # ................................ Conocer el total de goles de los equipos.
                        for equipo in torneo_elejido.equipos:
                            total_goles = sum(jugador.goles for jugador in equipo.integrantes)
                            print(f"El total de goles del equipo {equipo.nombre} es: {total_goles}")

                    elif operacion == 11:  # ................................ Generar rol de juegos.
                        pass

                    elif operacion == 12:  # ................................ Conocer el total de goles de los equipos.
                        print(f"Saliendo..")

        elif opcion == 3:  # ................................ Salir del programa.
            print("Saliendo del programa...")
        else:
            print("Opcion no valida, intente de nuevo")

            print()
            print(Fore.BLACK + "-----------------------------")
            print()

if __name__ == '__main__':
    main()
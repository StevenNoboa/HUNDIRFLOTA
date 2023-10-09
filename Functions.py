import random
import numpy as np
from variables import tablero_dimension, barcos
import time

# Función de bienvenida al juego
def bienvenido(nombre):
    time.sleep(1)
    print("Bienvenido a la aventura: ", nombre)
    time.sleep(1)
    print("¡Prepárate para hundir a la máquina!")
    time.sleep(1)
    print("¡El que hunda los barcos primero gana!, ¡A por todas!")

    return nombre

# Función que permite posicionar los barcos
def posicionar_barcos(tablero, longitud):
    direccion = random.choice(["N-S", "E-O"])
    barco = True

    while barco:
        fila = np.random.choice(10)
        columna = np.random.choice(10)

        if direccion == "N-S" and fila + longitud - 1 <= 9 and \
           len(tablero[np.where(tablero[fila:fila + longitud, columna] == "O")]) == 0:
            tablero[fila, columna] = "O"
            tablero[fila:fila + longitud, columna] = "O"
            barco = False
        elif direccion == "E-O" and columna + longitud - 1 <= 9 and \
             len(tablero[np.where(tablero[fila, columna:columna + longitud] == "O")]) == 0:
            tablero[fila, columna] = "O"
            tablero[fila, columna:columna + longitud] = "O"
            barco = False

# Función que permite el disparo del jugador
def disparo_jugador(tablero_maquina, tablero_oculto):
    print("Dispara:")
    fila = int(input("Introduce la fila del 1 al 10: "))
    columna = int(input("Introduce la columna del 1 al 10: "))

    h = (fila - 1, columna - 1)
    b = (fila, columna)
    time.sleep(2)
    if fila > 10 or columna > 10:
        print("Elige números del 1 al 10, pierdes el turno")
    elif tablero_maquina[h] == "_":
        tablero_maquina[h] = "A"
        tablero_oculto[h] = "A"
        print("Agua en la posición indicada:")
        print(tablero_oculto)
        print("Es el turno de la máquina")
        return "Agua"
    elif tablero_maquina[h] == "O":
        tablero_maquina[h] = "X"
        tablero_oculto[h] = "X"
        print("¡Objetivo alcanzado!. Tocado en la posición:", b)
        print(tablero_oculto)
        return "Tocado"
    else:
        print("Ya elegiste esa posición: pierdes el turno")

# Función que permite el disparo de la máquina
def disparo_maquina(tablero_jugador, lista_corrdenadas_maquina):
    disparo_aleatorio = random.choice(lista_corrdenadas_maquina)
    lista_corrdenadas_maquina.remove(disparo_aleatorio)
    time.sleep(2)
    if tablero_jugador[disparo_aleatorio] == "_":
        tablero_jugador[disparo_aleatorio] = "A"

        print("La máquina ha fallado, Agua en:", disparo_aleatorio, "Es tu turno:")
        print(tablero_jugador)
        return "Agua"
    elif tablero_jugador[disparo_aleatorio] == "O":
        tablero_jugador[disparo_aleatorio] = "X"

        print("La máquina ha acertado, tocado en:", disparo_aleatorio)
        print(tablero_jugador)
        return "Tocado"
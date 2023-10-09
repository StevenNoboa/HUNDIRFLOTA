import numpy as np
from variables import barcos, lista_corrdenadas_maquina
from Functions import bienvenido, posicionar_barcos, disparo_jugador, disparo_maquina
from clase_tablero import Tablero
import time

nombre_jugador = bienvenido(input("Introduce tu nombre de batalla: ")) # Nombre del jugador

# Se definen en las variables la clase Tablero
jugador = Tablero(nombre_jugador)
maquina = Tablero("Máquina")
tablero_oculto_maquina = Tablero("MaquinaOculto")

# Se emplea el método de .tablero para la creación de los tableros
tablero_jugador = jugador.tablero() # tablero del jugador
tablero_maquina = maquina.tablero() # tablero de la máquina
tablero_oculto = tablero_oculto_maquina.tablero()  # tablero oculto en el que se actualizará los disparos

# Bucle for empleado para pitar los barcos segun la longitud marca en la variable barcos
for longitud in barcos.values():
    posicionar_barcos(tablero_jugador, longitud) # se posicionan los barcos del jugador
    posicionar_barcos(tablero_maquina, longitud) # se posicionan los barcos de la máquina
time.sleep(2)
print("Este será tu tablero de batalla:", nombre_jugador)
print(tablero_jugador)
# comprobación si se descomenta para ver barcos en máquina
# print(tablero_maquina) 


# Sistema de turnos
final = False # el juego aún no termina
turno_jugador = True # el jugador comienza
while final == False:
    # Turno del jugador
    if turno_jugador == True:
        intento_jugador = disparo_jugador(tablero_maquina, tablero_oculto)
        time.sleep(3)
        if len(tablero_maquina[np.where(tablero_maquina == "O")]) == 0:
            print("Has hundido toda la flota, ¡Ganaste!")
            final = True # finaliza el juego
            break

        if intento_jugador == "Tocado":
            continue # El jugador tiene otro turno si acierta
    else:   
    # Turno de la máquina
        intento_maquina = disparo_maquina(tablero_jugador, lista_corrdenadas_maquina)
        time.sleep(3)
        if len(tablero_jugador[np.where(tablero_jugador == "O")]) == 0:
            print("Has perdido.")
            final = True # finaliza el juego
            break

        if intento_maquina == "Tocado":
            continue # La máquina tiene otro turno si acierta
    turno_jugador = False
print("Final de la partida")
import numpy as np

tablero_dimension = 10 # Tablero 10 X 10
barcos = {             # Tamaño de los barcos
    "barco_1": 4,
    "barco_2": 3,
    "barco_3": 2,
    "barco_4": 1 }

lista_corrdenadas_maquina = [(x, y) for x in range(10) for y in range(10)] # Puntos de disparo de la máquina
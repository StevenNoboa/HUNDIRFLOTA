import numpy as np
from variables import tablero_dimension

class Tablero: 
    def __init__(self, nombre):
        self.nombre = nombre

    def tablero(self):
        tablero = np.full((tablero_dimension, tablero_dimension), "_") 
        return tablero


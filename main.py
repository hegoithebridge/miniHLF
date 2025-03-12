from variables import *
from funciones import *
from clases import *

# import variables
# import funciones
# import clases

vidas_computer = 8
presentacion()
tablero_computer             = crear_tablero(TAMANO_TABLERO)
tablero_computer_visualizar  = crear_tablero(TAMANO_TABLERO)
posicionar_barcos_fijos(tablero_computer)
# Sólo para pruebas
visualizar_tablero(tablero_computer)

while vidas_computer > 0:
    print("Comienza tu turno")
    toques_jugador = jugar_contra_ordenador(tablero_computer,tablero_computer_visualizar)
    print("Has acertado",toques_jugador,"disparos")
    vidas_computer = vidas_computer - toques_jugador
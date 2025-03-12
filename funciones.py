import pprint
def visualizar_tablero(tablero):
    pprint.pprint(tablero)

def disparo(tablero,tablero_mostrar,i,j):
    if tablero[i][j] == 'B':
        print("Tocado")
        tablero[i][j] = "X"
        tablero_mostrar[i][j] = "X"
        return True
    elif tablero[i][j] == " ":
        print("Agua")
        tablero[i][j] = "O"
        tablero_mostrar[i][j] = "X"
        return False
    else:
        print("Ya habías disparado allí, inútil")
        return False
    
    
def posicionar_barcos_fijos(tablero):
    tablero[3][3] = 'B'
    tablero[4][3] = 'B'
    tablero[5][3] = 'B'
    tablero[6][3] = 'B'
    
    tablero[1][0] = 'B'
    tablero[1][1] = 'B'
    tablero[1][2] = 'B'
    tablero[1][3] = 'B'
    
def presentacion():
    print("Hundir la Flota")
    print("Bienvenido")
    
    
def crear_tablero(tamano):
    tablero = [[" " for i in range(tamano)] for j in range(tamano)]
    return tablero

def jugar_contra_ordenador(tablero,tablero_mostrar):
    visualizar_tablero(tablero_mostrar)
    toques = 0 
    while True:
        i = int(input("Introduce la fila, por favor: "))
        j = int(input("Introduce la columna, por favor: "))
        acertado = disparo(tablero,tablero_mostrar,i,j)
        visualizar_tablero(tablero_mostrar)
        if acertado:
            toques = toques + 1
        else: 
            break
    return toques
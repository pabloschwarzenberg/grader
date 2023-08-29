# Crea un programa capaz de resolver el juego conocido como la sopa de letras. Este juego consiste en un tablero de N x M 
# donde cada posición del tablero tiene una letra. El objetivo del juego es encontrar palabras dentro del tablero, 
# ya sea en forma horizontal (de izquierda a derecha), vertical (de arriba a abajo) o diagonal 
# (de esquina superior izquierda a esquina inferior derecha). 
# Tomando como ejemplo la sopa de letras descrita en este archivo implementa la función sopaletras(nombre_archivo,palabras) 
# que recibe como parámetro el nombre de un archivo con la sopa de letras (en el formato del ejemplo) y una lista de 
# palabras a buscar en la sopa de letras. La función debe retornar una lista de tuplas, con tres valores:

#     La palabra tal como la recibe la función en lista de palabras.
#     Una lista de dos enteros con la fila y columna inicial donde aparece la palabra
#     Un string que describe la dirección en la que aparece la palabra: "derecha", "abajo", "diagonal", de acuerdo a si la palabra aparece en forma horizontal, vertical o diagonal, respectivamente.

# Por ejemplo, la llamada sopaletras("sopa.txt",["casa"]) debería retornar una lista 
# con una tupla de tres elementos: [(casa,[0,0],"derecha")]


def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    matriz = []
    for linea in archivo:
        arr_letras = []
        for letra in linea:
            if letra != '\n' and letra != ' ' and letra != "":
                arr_letras.append(letra)
        matriz.append(arr_letras)

    # recorrer_matriz_horizontal(matriz, palabras)
    # recorrer_matriz_vertical(matriz, palabras)
    recorrer_matriz_diagonal(matriz, palabras)
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

def recorrer_matriz_diagonal(matriz, palabra):
    horizontal = len(matriz[0])
    vertical = len(matriz)
    i_index = 0
    j_index = 0
            
# C A S A
# E R G H
# I O A M

# 0,0  1,0  2,0  3,0
# 0,1  1,1  2,1  3,1
# 0,2  1,2  2,2  3,2
def recorrer_matriz_horizontal(matriz, palabras):
    for palabra in palabras:
        vertical = len(matriz)
        for i in range(vertical):
            p = "".join(matriz[i])
            if p == palabra:
                print(palabra)


def recorrer_matriz_vertical(matriz, palabras):
    horizontal = len(matriz[0])
    vertical = len(matriz)
    for palabra in palabras:
        for j in range(horizontal):
            p = ""
            for i in range(vertical):
                p = p + str(matriz[i][j])
            if p == palabra:
                print(p)


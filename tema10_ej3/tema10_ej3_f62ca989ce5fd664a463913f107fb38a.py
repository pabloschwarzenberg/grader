def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

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

sopaletras('sopa.txt', ['CASA', 'ARO'])
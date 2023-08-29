import random 


alfabeto=["A","C","E","S","R","G","H","I","O","M"

def crear_matrix(N):
    matrix =[]
    for i in range(N):
        matrix.append([])
        for j in range(N):
            matrix[i].append(" ")
            matrix[i][j]=alfabeto[random.randint(0, 11)]
    return matrix

def de_izquierda_a_derecha(matrix,palabra):
    for i in range(len(palabra)):
        matrix[N-1][i]= palabra[ i ]
    return matrix

def de_derecha_a_izquierda(matrix, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        matrix[N-3][i-len(palabra)]=palabra[i]
    return matrix

def de_arriba_abajo(matrix,palabra):
    for i in range(len(palabra)):
        matrix[i][N-1]= palabra[ i ]
    return matrix

def de_abajo_arriba(matrix, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        matrix[i-len(palabra)][N-3]=palabra[i]
    return matrix

def diagonal_de_arriba_abajo(matrix, palabra):
    for i in range(len(palabra)):
        matrix[i][i]= palabra[ i ]
    return matrix

def diagonal_de_abajo_arriba(matrix, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        matrix[i-len(palabra)][i]= palabra[ i ]
    return matrix   
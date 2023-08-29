# CODE START
import time
import random
import string

#============== Utilidad
from util import *
    
#============== Matriz

def crear_matrix(nxn):
    """Devuelve matrix de nxn filas/columnas."""
    matrix =[]
    for i in range(nxn):
        matrix.append([])
        for e in range(nxn):
            matrix[i].append("")
    return matrix

def completar_matrix(mtx, n, randomChar=True):
    """Completa y devuelve una matriz con letras aleatorias o con asteriscos.
    Parametros:
    mtx        -- matriz a completar
    n          -- entero de filas/columnas a completar
    randomChar -- booleano que indica si son letras aleatorias o asteriscos
    """
    for i in range(n):
        for e in range(n):
            if randomChar :
                if mtx[i][e] == "" : mtx[i][e] = random.choice(string.ascii_lowercase)
            else:
                if mtx[i][e] == "" : mtx[i][e] = "*"

    return mtx

def valores_posicion(matrix, nxn, isrow, pos):
    """Devuelve una lista con informacion acerca de una fila/columna especifica de la matriz.
    Parametros:
    isrow -- booleano que indica si es fila o columna
    pos   -- entero que indica fila/columna
    """
    
    valores = []
    espacios = 0
    for i in range(nxn):
        if isrow:
            if matrix[pos][i] != "":
                valores.append(espacios)
                valores.append(matrix[pos][i])
            else:
                espacios+=1
        else:
            if matrix[i][pos] != "":
                valores.append(espacios)
                valores.append(matrix[i][pos])
                espacios = 0
            else:
                espacios+=1

    # Si la fila/columna esta vacia, indicar que existen nxn espacios vacios
    if espacios == nxn :
        valores.append(espacios)
        valores.append("0")

    return valores

def procesar_palabras(matrix, nxn, palabras):
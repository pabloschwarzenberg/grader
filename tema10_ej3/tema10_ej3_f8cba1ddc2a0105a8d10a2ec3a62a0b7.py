def buscar_palabra(tablero, palabra, fila, columna, direccion):
    """
    Busca una palabra en una dirección específica a partir de una posición inicial (fila, columna) en un tablero dado.
    Retorna True si encuentra la palabra, False en caso contrario.
    """
    if direccion == "derecha":
# Verificar si la palabra cabe en la dirección derecha
    if columna + len(palabra) > len(tablero[0]):
            return False
# Verificar si la palabra está en la dirección derecha
        for i in range(len(palabra)):
    if tablero[fila][columna + i] != palabra[i]:
                return False
        return True
    elif direccion == "abajo":
# Verificar si la palabra está en la dirección abajo
        for i in range(len(palabra)):
     if tablero[fila + i][columna] != palabra[i]:
        return False
        return True
    elif direccion == "diagonal":
# Verificar si la palabra está en la dirección diagonal
        for i in range(len(palabra)):
      if tablero[fila + i][columna + i] != palabra[i]:
        return False
        return True
def buscar_en_tablero(tablero, palabra):
    """
    Busca una palabra en todas las direcciones posibles en un tablero dado.
    Retorna una lista con todas las posiciones donde aparece la palabra y la dirección en la que aparece.
    """
      if posiciones = []
        for i in range(len(tablero)):
        for j in range(len(tablero[0])):
      if buscar_palabra(tablero, palabra, i, j, "derecha"):
                posiciones.append((i, j, "derecha"))
      if buscar_palabra(tablero, palabra, i, j, "abajo"):
                posiciones.append((i, j, "abajo"))
      if buscar_palabra(tablero, palabra, i, j, "diagonal"):
                posiciones.append((i, j, "diagonal"))
    return posiciones

def sopaletras(nombre_archivo, palabras):
    """
    Busca las palabras dadas en una sopa de letras en un archivo dado.
    Retorna una lista de tuplas con la palabra, su posición inicial y la dirección en la que aparece.
    """
    with open(nombre_archivo, "r") as f:
        tablero = [list(linea.strip()) for linea in f.readlines()]
    resultados = []
    for palabra in palabras:
        posiciones = buscar_en_tablero(tablero, palabra)
        if len(posiciones) > 0:
            resultados.append((palabra, posiciones[0][:2], posiciones[0][2]))
    return resultados
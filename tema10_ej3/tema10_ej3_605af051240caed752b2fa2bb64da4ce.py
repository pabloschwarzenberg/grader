def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = []
        for linea in archivo:
            fila = linea.strip().split(',')
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra):
    filas = len(sopa)
    columnas = len(sopa[0])
    longitud = len(palabra)

    for fila in range(filas):
        for columna in range(columnas):
            # Buscar horizontalmente
            if columna + longitud <= columnas:
                if sopa[fila][columna:columna+longitud] == palabra:
                    return [fila, columna], "derecha"

            # Buscar verticalmente
            if fila + longitud <= filas:
                if all(sopa[fila+i][columna] == palabra[i] for i in range(longitud)):
                    return [fila, columna], "abajo"

            # Buscar en diagonal hacia abajo
            if columna + longitud <= columnas and fila + longitud <= filas:
                if all(sopa[fila+i][columna+i] == palabra[i] for i in range(longitud)):
                    return [fila, columna], "diagonal"

            # Buscar en diagonal hacia arriba
            if columna + longitud <= columnas and fila >= longitud - 1:
                if all(sopa[fila-i][columna+i] == palabra[i] for i in range(longitud)):
                    return [fila, columna], "diagonal"

    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        posicion = buscar_palabra(sopa, palabra)
        if posicion:
            resultados.append((palabra, posicion[0], posicion[1]))
    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)

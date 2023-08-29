def cargar_sopa(nombre_archivo):
    sopa = []

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)

    return sopa


def buscar_palabra(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])

    for fila in range(n_filas):
        for columna in range(n_columnas):
            if sopa[fila][columna] == palabra[0]:
                # Verificar horizontal derecha
                if columna + len(palabra) <= n_columnas and sopa[fila][columna:columna + len(palabra)] == palabra:
                    return [fila, columna], "derecha"
                
                # Verificar vertical abajo
                if fila + len(palabra) <= n_filas:
                    palabra_vertical = [sopa[fila + i][columna] for i in range(len(palabra))]
                    if palabra_vertical == palabra:
                        return [fila, columna], "abajo"

                # Verificar diagonal derecha
                if columna + len(palabra) <= n_columnas and fila + len(palabra) <= n_filas:
                    palabra_diagonal = [sopa[fila + i][columna + i] for i in range(len(palabra))]
                    if palabra_diagonal == palabra:
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


# Ejemplo de uso
nombre_archivo = "sopa.txt"
palabras_buscar = ["casa"]

resultado = sopaletras(nombre_archivo, palabras_buscar)

print(resultado)

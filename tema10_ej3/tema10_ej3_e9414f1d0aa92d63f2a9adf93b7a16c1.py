def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo.readlines()]

    # Dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    # Direcciones posibles: derecha, abajo, diagonal
    direcciones = [(1, 0), (0, 1), (1, 1)]

    # Lista para almacenar los resultados
    resultados = []

    # Recorrer todas las palabras a buscar
    for palabra in palabras:
        # Convertir la palabra en una lista de letras
        letras = list(palabra)

        # Buscar la palabra en la sopa de letras
        for i in range(filas):
            for j in range(columnas):
                # Verificar en todas las direcciones posibles
                for direccion in direcciones:
                    dx, dy = direccion
                    encontrada = True

                    # Verificar si la palabra aparece en la dirección actual
                    for k in range(len(letras)):
                        if i + k*dx >= filas or j + k*dy >= columnas or sopa[i + k*dx][j + k*dy] != letras[k]:
                            encontrada = False
                            break

                    # Si se encontró la palabra, agregar los resultados
                    if encontrada:
                        resultado = (palabra, [i, j], direccion_texto(direccion))
                        resultados.append(resultado)

    return resultados

def direccion_texto(direccion):
    dx, dy = direccion
    if dx == 1 and dy == 0:
        return "derecha"
    elif dx == 0 and dy == 1:
        return "abajo"
    elif dx == 1 and dy == 1:
        return "diagonal"

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]

    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)

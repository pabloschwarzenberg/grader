def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        sopa = [list(linea.strip()) for linea in archivo]

    # Obtener dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    # Definir las direcciones posibles: derecha, abajo y diagonal
    direcciones = [(0, 1), (1, 0), (1, 1)]

    # Lista para almacenar los resultados
    resultados = []

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                for direccion in direcciones:
                    dx, dy = direccion
                    fin_fila = fila + dx * (len(palabra) - 1)
                    fin_columna = columna + dy * (len(palabra) - 1)

                    # Verificar si la palabra cabe en la dirección actual
                    if 0 <= fin_fila < filas and 0 <= fin_columna < columnas:
                        encontrada = True

                        # Verificar si la palabra aparece en la dirección actual
                        for i in range(len(palabra)):
                            if sopa[fila + i * dx][columna + i * dy] != palabra[i]:
                                encontrada = False
                                break

                        # Si la palabra se encontró, agregarla a los resultados
                        if encontrada:
                            posicion_inicial = [fila, columna]
                            direccion_str = obtener_direccion(dx, dy)
                            resultados.append((palabra, posicion_inicial, direccion_str))

    return resultados

def obtener_direccion(dx, dy):
    if dx == 0 and dy == 1:
        return "derecha"
    elif dx == 1 and dy == 0:
        return "abajo"
    elif dx == 1 and dy == 1:
        return "diagonal"

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)
  
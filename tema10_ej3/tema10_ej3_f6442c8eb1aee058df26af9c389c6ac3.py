def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y almacenar la sopa de letras en una matriz
    with open(nombre_archivo, 'r') as file:
        sopa = [list(line.strip()) for line in file]

    # Obtener las dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])

    # Definir las direcciones posibles: derecha, abajo, diagonal derecha y diagonal izquierda
    direcciones = [(1, 0), (0, 1), (1, 1), (-1, 1)]

    resultados = []

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                for direccion in direcciones:
                    dx, dy = direccion
                    # Verificar si la palabra cabe en la dirección actual
                    if i + dx*(len(palabra)-1) < filas and j + dy*(len(palabra)-1) < columnas:
                        # Verificar si la palabra coincide en la dirección actual
                        coincidencia = True
                        for k in range(len(palabra)):
                            if sopa[i + k*dx][j + k*dy] != palabra[k]:
                                coincidencia = False
                                break
                        # Si hay coincidencia, agregar la tupla a la lista de resultados
                        if coincidencia:
                            direccion_str = 'derecha' if dx == 1 and dy == 0 else 'abajo' if dx == 0 and dy == 1 else 'diagonal'
                            resultados.append((palabra, [i, j], direccion_str))

    return resultados

# Prueba del programa
if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultados)
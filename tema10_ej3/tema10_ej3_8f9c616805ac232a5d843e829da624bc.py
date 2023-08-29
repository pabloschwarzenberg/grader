def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    tablero = []
    for linea in archivo:
        fila = linea.strip().split(",")
        tablero.append(fila)
    archivo.close()

    filas = len(tablero)
    columnas = len(tablero[0])
    direcciones = ["derecha", "abajo", "diagonal"]
    resultados = []

    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                # Verificar horizontalmente
                if j + len(palabra) <= columnas:
                    if "".join(tablero[i][j : j + len(palabra)]) == palabra:
                        resultados.append((palabra, [i, j], direcciones[0]))

                # Verificar verticalmente
                if i + len(palabra) <= filas:
                    columna = [tablero[k][j] for k in range(i, i + len(palabra))]
                    if "".join(columna) == palabra:
                        resultados.append((palabra, [i, j], direcciones[1]))

                # Verificar diagonalmente
                if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                    diagonal = [
                        tablero[i + k][j + k] for k in range(len(palabra))
                    ]
                    if "".join(diagonal) == palabra:
                        resultados.append((palabra, [i, j], direcciones[2]))

    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    for resultado in resultados:
        print(resultado)

           
def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    tablero = [linea.strip().split() for linea in archivo]
    archivo.close()

    n = len(tablero)
    m = len(tablero[0])

    resultados = []

    for palabra in palabras:
        for i in range(n):
            for j in range(m):
                if tablero[i][j] == palabra[0]:
                    # Buscar en dirección horizontal (derecha)
                    if j + len(palabra) <= m and tablero[i][j:j + len(palabra)] == list(palabra):
                        resultados.append((palabra, [i, j], "derecha"))
                    # Buscar en dirección vertical (abajo)
                    if i + len(palabra) <= n and [tablero[x][j] for x in range(i, i + len(palabra))] == list(palabra):
                        resultados.append((palabra, [i, j], "abajo"))
                    # Buscar en dirección diagonal (derecha-abajo)
                    if i + len(palabra) <= n and j + len(palabra) <= m and [tablero[i + x][j + x] for x in range(len(palabra))] == list(palabra):
                        resultados.append((palabra, [i, j], "diagonal"))

    return resultados

if __name__ == "__main__":
    resultado = sopaletras("sopa.txt", ["casa"])
    print(resultado)

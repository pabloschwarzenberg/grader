def sopaletras(archivo, palabras):
    texto = open(archivo, "r")
    tablero = []
    for linea in texto:
        fila = linea.strip().split()
        tablero.append(fila)
    texto.close()
    respuestas = []
    filas = len(tablero)
    columnas = len(tablero[0])
    for palabra in palabras:
        palabra = palabra.upper()
        letras_encontradas = False
        for i in range(filas):
            for j in range(columnas):
                if tablero[i][j] == palabra[0]:
                    if j + len(palabra) <= columnas and all(tablero[i][j+k] == palabra[k] for k in range(len(palabra))):
                        respuestas.append((palabra.lower(), [i, j], "derecha"))
                        letras_encontradas = True
                    if i + len(palabra) <= filas and all(tablero[i+k][j] == palabra[k] for k in range(len(palabra))):
                        respuestas.append((palabra.lower(), [i, j], "abajo"))
                        letras_encontradas = True
                    if i + len(palabra) <= filas and j + len(palabra) <= columnas and all(tablero[i+k][j+k] == palabra[k] for k in range(len(palabra))):
                        respuestas.append((palabra.lower(), [i, j], "diagonal"))
                        letras_encontradas = True
                if letras_encontradas:
                    break
            if letras_encontradas:
                break
    return respuestas

if __name__ == '__main__':
    print(sopaletras("sopa.txt", ["cra"])[0])
    print(sopaletras("sopa.txt", ["aro"])[0])
    print(sopaletras("sopa.txt", ["casa"])[0])
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))

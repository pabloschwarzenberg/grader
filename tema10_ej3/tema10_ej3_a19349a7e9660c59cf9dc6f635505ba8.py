def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, 'r') as file:
        sopa = [list(line.strip().replace(" ", "")) for line in file]

    filas = len(sopa)
    columnas = len(sopa[0])

    resultados = []

    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                # Buscar horizontalmente hacia la derecha
                if j + len(palabra) <= columnas:
                    if ''.join(sopa[i][j:j+len(palabra)]) == palabra:
                        resultados.append((palabra, [i, j], "derecha"))
                # Buscar diagonalmente hacia abajo y hacia la derecha
                if i + len(palabra) <= filas and j + len(palabra) <= columnas:
                    if ''.join(sopa[i+k][j+k] for k in range(len(palabra))) == palabra:
                        resultados.append((palabra, [i, j], "diagonal"))
                # Buscar verticalmente hacia abajo
                if i + len(palabra) <= filas:
                    if ''.join(sopa[i+k][j] for k in range(len(palabra))) == palabra:
                        resultados.append((palabra, [i, j], "abajo"))

    return resultados


if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]

    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)

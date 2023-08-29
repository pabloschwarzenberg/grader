def sopaletras(sopa, palabras):
    filas = len(sopa)
    columnas = len(sopa[0])

    direcciones = {'derecha': (0, 1), 'abajo': (1, 0), 'diagonal': (1, 1)}

    resultados = []

    for palabra in palabras:
        encontrada = False

        for i in range(filas):
            for j in range(columnas - len(palabra) + 1):
                if sopa[i][j:j + len(palabra)] == list(palabra):
                    resultados.append((palabra, [i, j], 'derecha'))
                    encontrada = True
                    break
            if encontrada:
                break

        if not encontrada:
            for i in range(filas - len(palabra) + 1):
                for j in range(columnas):
                    columna = [sopa[k][j] for k in range(i, i + len(palabra))]
                    if columna == list(palabra):
                        resultados.append((palabra, [i, j], 'abajo'))
                        encontrada = True
                        break
                if encontrada:
                    break

        if not encontrada:
            for i in range(filas - len(palabra) + 1):
                for j in range(columnas - len(palabra) + 1):
                    diagonal = [sopa[i + k][j + k] for k in range(len(palabra))]
                    if diagonal == list(palabra):
                        resultados.append((palabra, [i, j], 'diagonal'))
                        encontrada = True
                        break
                if encontrada:
                    break

    return resultados

sopa = [
    ['c', 'a', 's', 'a'],
    ['a', 'r', 'o', 'c'],
    ['r', 'a', 'c', 'r'],
]

resultados = sopaletras(sopa, ["casa", "cra", "aro"])

for resultado in resultados:
    print(resultado)

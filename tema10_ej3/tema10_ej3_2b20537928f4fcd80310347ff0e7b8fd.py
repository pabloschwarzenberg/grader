def sopaletras(nombre_archivo, palabras):
    matriz = []
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            linea = linea.strip()
            fila = list(linea)
            matriz.append(fila)
    n = len(matriz)
    m = len(matriz[0])
    resultados = []
    for palabra in palabras:
        palabra = palabra.upper()
        l = len(palabra)
        encontrada = False
        for i in range(n):
            for j in range(m):
                if encontrada:
                    break
                if matriz[i][j] == palabra[0]:
                    if j + l <= m:
                        coincide = True
                        for k in range(1, l):
                            if matriz[i][j + k] != palabra[k]:
                                coincide = False
                                break
                        if coincide:
                            resultado = (palabra, [i, j], "derecha")
                            resultados.append(resultado)
                            encontrada = True
                    if i + l <= n:
                        coincide = True
                        for k in range(1, l):
                            if matriz[i + k][j] != palabra[k]:
                                coincide = False
                                break
                        if coincide:
                            resultado = (palabra, [i, j], "abajo")
                            resultados.append(resultado)
                            encontrada = True
                    if i + l <= n and j + l <= m:
                        coincide = True
                        for k in range(1, l):
                            if matriz[i + k][j + k] != palabra[k]:
                                coincide = False
                                break
                        if coincide:
                            resultado = (palabra, [i, j], "diagonal")
                            resultados.append(resultado)
                            encontrada = True
        if not encontrada:
            resultado = (palabra, [], "")
            resultados.append(resultado)
    return resultados

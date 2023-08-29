def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as archivo:
        sopa = [list(linea.strip()) for linea in archivo]
    n = len(sopa)
    m = len(sopa[0])
    resultados = []
    for palabra in palabras:
        for i in range(n):
            for j in range(m):
                # Buscar a la derecha
                if j + len(palabra) <= m and sopa[i][j:j+len(palabra)] == list(palabra):
                    resultados.append((palabra, [i, j], "derecha"))
                # Buscar abajo
                if i + len(palabra) <= n and [sopa[k][j] for k in range(i, i+len(palabra))] == list(palabra):
                    resultados.append((palabra, [i, j], "abajo"))
                # Buscar diagonal
                if i + len(palabra) <= n and j + len(palabra) <= m and [sopa[i+k][j+k] for k in range(len(palabra))] == list(palabra):
                    resultados.append((palabra, [i, j], "diagonal"))
    return resultados

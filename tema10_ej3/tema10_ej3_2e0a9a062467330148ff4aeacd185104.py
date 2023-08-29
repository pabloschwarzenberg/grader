def sopaletras(nombre_archivo, palabras):
    
    with open(nombre_archivo, 'r') as file:
        sopa = [list(line.strip()) for line in file]

    
    filas = len(sopa)
    columnas = len(sopa[0])

    
    def buscar_palabra(palabra, fila, columna, dir_fila, dir_columna):
        for letra in palabra:
            if fila < 0 or columna < 0 or fila >= filas or columna >= columnas or sopa[fila][columna] != letra:
                return False
            fila += dir_fila
            columna += dir_columna
        return True

    
    def buscar_palabra_en_sopa(palabra):
        for i in range(filas):
            for j in range(columnas):
                
                if buscar_palabra(palabra, i, j, 0, 1):
                    return [i, j], "derecha"
                
                if buscar_palabra(palabra, i, j, 1, 0):
                    return [i, j], "abajo"
                
                if buscar_palabra(palabra, i, j, 1, 1):
                    return [i, j], "diagonal"

        return None

    resultados = []
    
    for palabra in palabras:
        posicion = buscar_palabra_en_sopa(palabra)
        if posicion is not None:
            resultados.append((palabra, posicion[0], posicion[1]))

    return resultados
resultados = sopaletras("sopa.txt", ["casa"])
print(resultados)



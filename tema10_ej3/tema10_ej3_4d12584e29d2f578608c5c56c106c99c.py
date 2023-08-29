def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y almacenar la sopa de letras en una matriz
    with open(nombre_archivo, "r") as f:
        sopa = [list(linea.strip()) for linea in f.readlines()]
    n = len(sopa)
    m = len(sopa[0])
    
    # Función auxiliar para buscar en una dirección
    def buscar_palabra(palabra, i, j, di, dj):
        for k in range(len(palabra)):
            if i < 0 or j < 0 or i >= n or j >= m or sopa[i][j] != palabra[k]:
                return False
            i += di
            j += dj
        return True
    
    # Buscar las palabras en la sopa de letras
    resultados = []
    for palabra in palabras:
        for i in range(n):
            for j in range(m):
                if buscar_palabra(palabra, i, j, 1, 0):
                    resultados.append((palabra, [i, j], "abajo"))
                elif buscar_palabra(palabra, i, j, 0, 1):
                    resultados.append((palabra, [i, j], "derecha"))
                elif buscar_palabra(palabra, i, j, 1, 1):
                    resultados.append((palabra, [i, j], "diagonal"))
    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "perro", "gato", "raton"])
    print(resultados)
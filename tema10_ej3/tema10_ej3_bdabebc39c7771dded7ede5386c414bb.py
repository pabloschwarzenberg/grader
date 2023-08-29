def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])

    # Buscar palabra horizontalmente
    for i in range(n):
        for j in range(m - len(palabra) + 1):
            if sopa[i][j:j+len(palabra)] == palabra:
                return [i, j], "derecha"

    # Buscar palabra verticalmente
    for i in range(n - len(palabra) + 1):
        for j in range(m):
            columna = [sopa[i+k][j] for k in range(len(palabra))]
            if columna == list(palabra):
                return [i, j], "abajo"

    # Buscar palabra en diagonal (esquina superior izquierda a esquina inferior derecha)
    for i in range(n - len(palabra) + 1):
        for j in range(m - len(palabra) + 1):
            diagonal = [sopa[i+k][j+k] for k in range(len(palabra))]
            if diagonal == list(palabra):
                return [i, j], "diagonal"

    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []

    for palabra in palabras:
        posicion = buscar_palabra(sopa, palabra)
        if posicion:
            resultados.append((palabra, posicion[0], posicion[1]))

    return resultados


if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa"]
    resultados = sopaletras(archivo_sopa, palabras_buscar)
    print(resultados)

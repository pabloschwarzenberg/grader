def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra, fila, columna, direccion):
    dx, dy = direccion
    filas = len(sopa)
    columnas = len(sopa[0])

    for letra in palabra:
        if fila < 0 or columna < 0 or fila >= filas or columna >= columnas or sopa[fila][columna] != letra:
            return False
        fila += dx
        columna += dy

    return True

def obtener_direccion_string(direccion):
    if direccion == (0, 1):
        return "derecha"
    elif direccion == (1, 0):
        return "abajo"
    elif direccion == (1, 1):
        return "diagonal"

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    filas = len(sopa)
    columnas = len(sopa[0])
    direcciones = [(0, 1), (1, 0), (1, 1)]
    resultados = []

    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                for direccion in direcciones:
                    if buscar_palabra(sopa, palabra, fila, columna, direccion):
                        resultado = (palabra, [fila, columna], obtener_direccion_string(direccion))
                        resultados.append(resultado)

    return resultados

if __name__ == "__main__":
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)

def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]
    
    # Obtener las dimensiones del tablero
    filas = len(sopa)
    columnas = len(sopa[0])
    
    # Definir las direcciones posibles
    direcciones = {
        "derecha": (0, 1),
        "abajo": (1, 0),
        "diagonal": (1, 1)
    }
    
    resultados = []
    
    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        for i in range(filas):
            for j in range(columnas):
                for direccion, (dx, dy) in direcciones.items():
                    # Verificar si la palabra aparece en la dirección actual
                    if es_palabra(sopa, palabra, i, j, dx, dy):
                        resultados.append((palabra, [i, j], direccion))
    
    return resultados


def es_palabra(sopa, palabra, fila, columna, dx, dy):
    # Obtener las dimensiones del tablero
    filas = len(sopa)
    columnas = len(sopa[0])
    
    # Calcular el número de letras de la palabra
    longitud = len(palabra)
    
    # Verificar que la palabra no se salga del tablero en la dirección actual
    if (
        fila + (longitud - 1) * dx >= filas or
        columna + (longitud - 1) * dy >= columnas
    ):
        return False
    
    # Verificar si la palabra aparece en la dirección actual
    for i in range(longitud):
        if sopa[fila + i * dx][columna + i * dy] != palabra[i]:
            return False
    
    return True


if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de la sopa de letras: ")
    palabras = input("Ingrese las palabras a buscar (separadas por espacios): ").split()
    
    resultados = sopaletras(nombre_archivo, palabras)
    
    print("Resultados:")
    for palabra, posicion, direccion in resultados:
        print(palabra, posicion, direccion)
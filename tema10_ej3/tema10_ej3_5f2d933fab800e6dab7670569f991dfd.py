def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y almacenar el tablero
    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()

    # Eliminar los caracteres de nueva línea y dividir en letras
    tablero = [list(line.strip().split()) for line in lines]

    # Obtener las dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0])

    # Convertir todas las palabras a minúsculas
    palabras = [palabra.lower() for palabra in palabras]

    # Definir las direcciones posibles
    direcciones = [(0, 1), (1, 0), (1, 1)]

    # Lista de resultados
    resultados = []

    # Función auxiliar para comprobar si una posición es válida en el tablero
    def es_valida(fila, columna):
        return 0 <= fila < filas and 0 <= columna < columnas

    # Función auxiliar para buscar una palabra en una dirección determinada
    def buscar_palabra(palabra, fila, columna, direccion):
        dx, dy = direccion
        longitud = len(palabra)
        ultima_fila = fila + (longitud - 1) * dx
        ultima_columna = columna + (longitud - 1) * dy

        # Comprobar si la palabra cabe en la dirección especificada
        if not es_valida(ultima_fila, ultima_columna):
            return False

        # Verificar si la palabra coincide en la dirección especificada
        for i in range(longitud):
            nueva_fila = fila + i * dx
            nueva_columna = columna + i * dy
            if tablero[nueva_fila][nueva_columna].lower() != palabra[i]:
                return False

        return True

    # Buscar cada palabra en el tablero
    for palabra in palabras:
        for fila in range(filas):
            for columna in range(columnas):
                for direccion in direcciones:
                    if buscar_palabra(palabra, fila, columna, direccion):
                        # Convertir la dirección a cadena
                        direccion_str = ""
                        if direccion == (0, 1):
                            direccion_str = "derecha"
                        elif direccion == (1, 0):
                            direccion_str = "abajo"
                        else:
                            direccion_str = "diagonal"

                        # Agregar la palabra, posición inicial y dirección a los resultados
                        resultados.append((palabra, [fila, columna], direccion_str))

    return resultados

def main():
    nombre_archivo = "sopa.txt"
    palabras = ["casa"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)

if __name__ == "__main__":
    main()
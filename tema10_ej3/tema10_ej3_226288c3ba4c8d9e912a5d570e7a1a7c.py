def sopaletras(nombre_archivo, palabras):
    sopa = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            sopa.append(linea.strip().split())

    n = len(sopa)
    m = len(sopa[0])

    direcciones = {
        "derecha": (0, 1),
        "abajo": (1, 0),
        "diagonal": (1, 1)
    }

    resultados = []

    for palabra in palabras:
        for i in range(n):
            for j in range(m):
                for direccion, (dx, dy) in direcciones.items():
                    fila = i
                    columna = j
                    k = 0

                    while k < len(palabra) and fila < n and columna < m and sopa[fila][columna] == palabra[k]:
                        fila += dx
                        columna += dy
                        k += 1

                    if k == len(palabra):
                        resultados.append((palabra, [i, j], direccion))

    return resultados


if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    palabras = input("Ingrese las palabras separadas por comas: ").split(",")

    resultado = sopaletras(nombre_archivo, palabras)
    print("Resultados:")
    for palabra, posicion, direccion in resultado:
        print(palabra, posicion, direccion)
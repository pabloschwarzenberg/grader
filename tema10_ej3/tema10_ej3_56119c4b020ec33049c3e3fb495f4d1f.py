def sopaletras(nombre_archivo,palabra):

    palabra = "".join(palabra)

    with open(nombre_archivo,"r") as archivo:

        sopaa = archivo.read()

        sopa = []
        lista = []

        for i in range(len(sopaa)):
            if sopaa[i] != "\n" and sopaa[i] != " ":
                lista.append(sopaa[i])

        sublista1 = lista[:4]
        sublista2 = lista[4:2*4]
        sublista3 = lista[2*4:]

        sopa.append(sublista1)
        sopa.append(sublista2)
        sopa.append(sublista3)

        print(sopa)

        palabra = palabra.upper()  # Convertir la palabra a mayúsculas para facilitar la comparación
        filas = len(sopa)
        columnas = len(sopa[0])
        
        # Buscar la palabra en forma horizontal
        for i in range(filas):
            fila = sopa[i]
            palabra_encontrada = ''.join(fila)
            if palabra_encontrada == palabra:
                return (palabra.lower(), [i, 0], "derecha")
        
        # Buscar la palabra en forma vertical
        for j in range(columnas):
            columna = [sopa[i][j] for i in range(filas)]
            palabra_encontrada = ''.join(columna)
            if palabra_encontrada == palabra:
                return (palabra.lower(), [0, j], "abajo")
        
        # Buscar la palabra en forma diagonal (de izquierda a derecha)
        for i in range(filas):
            for j in range(columnas):
                palabra_encontrada = ''
                k = 0
                while i + k < filas and j + k < columnas:
                    palabra_encontrada += sopa[i + k][j + k]
                    if palabra_encontrada == palabra:
                        return (palabra.lower(), [i, j], "diagonal")
                    k += 1
        
        return []  # La palabra no se encontró

 
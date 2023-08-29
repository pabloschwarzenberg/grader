def sopaletras(nombre_archivo, palabras):
    # Leer el archivo y obtener la sopa de letras
        sopa = [linea.strip().split(',') for linea in archivo]
    
    # Dimensiones de la sopa de letras
    filas = len(sopa)
    columnas = len(sopa[0])
    
    # Direcciones posibles: derecha, abajo, diagonal
    direcciones = [(0, 1), (1, 0), (1, 1)]
    
    resultados = []
    
    for palabra in palabras:
        # Buscar la palabra en la sopa de letras
        for i in range(filas):
            for j in range(columnas):
                for direccion in direcciones:
                    dx, dy = direccion
                    fin_fila = i + dx * (len(palabra) - 1)
                    fin_columna = j + dy * (len(palabra) - 1)
                    
                    # Verificar si la palabra cabe en la dirección actual
                    if fin_fila >= 0 and fin_fila < filas and fin_columna >= 0 and fin_columna < columnas:
                        encontrado = True
                        for k in range(len(palabra)):
                            fila = i + dx * k
                            columna = j + dy * k
                            if sopa[fila][columna] != palabra[k]:
                                encontrado = False
                                break
                        
                        # Si la palabra fue encontrada, guardar los resultados
                        if encontrado:
                            posicion_inicial = [i, j]
                            if direccion == (0, 1):
                                direccion_texto = "derecha"
                            elif direccion == (1, 0):
                                direccion_texto = "abajo"
                            else:
                                direccion_texto = "diagonal"
                            
                            resultados.append((palabra, posicion_inicial, direccion_texto))
    
    return resultados

if __name__ == "__main__":
    archivo = """C A S A
E R G H
I O A M"""
    palabras = ["casa"]
    
    resultados = sopaletras(archivo, palabras)
    
    for resultado in resultados:
        palabra, posicion, direccion = resultado
        print(palabra, posicion, direccion)


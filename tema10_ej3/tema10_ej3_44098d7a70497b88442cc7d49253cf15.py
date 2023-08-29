def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras y construir la matriz
    matriz = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            matriz.append(fila)
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    resultados = []
    
    # Función para buscar una palabra en una dirección específica
    def buscar_palabra(palabra, fila_inicial, col_inicial, dir_fila, dir_col):
        fila_actual = fila_inicial
        col_actual = col_inicial
        
        for letra in palabra:
            if fila_actual < 0 or fila_actual >= filas or col_actual < 0 or col_actual >= columnas or matriz[fila_actual][col_actual].lower() != letra:
                return False
            fila_actual += dir_fila
            col_actual += dir_col
        
        return True
    
    # Función para determinar la dirección de una palabra
    def determinar_direccion(fila_inicial, col_inicial, fila_final, col_final):
        if fila_inicial == fila_final:
            return "derecha"
        elif col_inicial == col_final:
            return "abajo"
        else:
            return "diagonal"
    
    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para ignorar mayúsculas
        
        for fila in range(filas):
            for col in range(columnas):
                if buscar_palabra(palabra, fila, col, 0, 1):  # Buscar horizontalmente (derecha)
                    direccion = determinar_direccion(fila, col, fila, col+len(palabra)-1)
                    resultados.append((palabra, [fila, col], direccion))
                
                if buscar_palabra(palabra, fila, col, 1, 0):  # Buscar verticalmente (abajo)
                    direccion = determinar_direccion(fila, col, fila+len(palabra)-1, col)
                    resultados.append((palabra, [fila, col], direccion))
                
                if buscar_palabra(palabra, fila, col, 1, 1):  # Buscar en diagonal (abajo y derecha)
                    direccion = determinar_direccion(fila, col, fila+len(palabra)-1, col+len(palabra)-1)
                    resultados.append((palabra, [fila, col], direccion))
    
    return resultados

# Prueba de la función sopaletras con ejemplo proporcionado
if __name__ == "__main__":
    resultado = sopaletras("sopa.txt", ["casa", "cra", "aro"])
    print(resultado)

           
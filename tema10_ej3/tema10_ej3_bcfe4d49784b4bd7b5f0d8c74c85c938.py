def leer_sopa(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        sopa = []
        for linea in archivo:
            fila = linea.strip().split(",")
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            if sopa[i][j] == palabra[0]:
                # Verificar si la palabra aparece hacia la derecha
                if j + len(palabra) <= n_columnas and sopa[i][j:j+len(palabra)] == palabra:
                    return (i, j, "derecha")
                # Verificar si la palabra aparece hacia abajo
                if i + len(palabra) <= n_filas and [sopa[k][j] for k in range(i, i+len(palabra))] == list(palabra):
                    return (i, j, "abajo")
                # Verificar si la palabra aparece en diagonal hacia abajo y a la derecha
                if i + len(palabra) <= n_filas and j + len(palabra) <= n_columnas and [sopa[i+k][j+k] for k in range(len(palabra))] == list(palabra):
                    return (i, j, "diagonal")
                # Verificar si la palabra aparece en diagonal hacia arriba y a la derecha
                if i - len(palabra) >= -1 and j + len(palabra) <= n_columnas and [sopa[i-k][j+k] for k in range(len(palabra))] == list(palabra)[::-1]:
                    return (i, j, "diagonal")
    return None
    
def sopaletras(nombre_archivo, palabras):
    sopa = leer_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        posicion = buscar_palabra(sopa, palabra)
        if posicion is not None:
            resultados.append((palabra, [posicion[0], posicion[1]], posicion[2]))
    return resultados
    
if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa", "auto", "computadora", "python"])
    print(resultados)
    
def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split(',')
            sopa.append(fila)
    return sopa

def buscar_palabra(sopa, palabra):
    n = len(sopa)
    m = len(sopa[0])
    for i in range(n):
        for j in range(m):
            # Buscar palabra en dirección derecha
            if j + len(palabra) <= m and ''.join(sopa[i][j:j+len(palabra)]) == palabra:
                return [i, j], "derecha"
            
            # Buscar palabra en dirección abajo
            if i + len(palabra) <= n and ''.join(sopa[k][j] for k in range(i, i+len(palabra))) == palabra:
                return [i, j], "abajo"
            
            # Buscar palabra en dirección diagonal hacia abajo y derecha
            if i + len(palabra) <= n and j + len(palabra) <= m and ''.join(sopa[i+k][j+k] for k in range(len(palabra))) == palabra:
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
    nombre_archivo = "sopa.txt"
    palabras = ["casa", "cra", "aro"]
    resultados = sopaletras(nombre_archivo, palabras)
    print(resultados)

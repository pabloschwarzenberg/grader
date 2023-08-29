def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = []
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
        return sopa

def buscar_horizontal(palabra, sopa):
    for i in range(len(sopa)):
        fila = sopa[i]
        for j in range(len(fila)):
            if fila[j] == palabra[0]:
                if j + len(palabra) <= len(fila) and fila[j:j+len(palabra)] == palabra:
                    return [i, j], "derecha"
    return None

def buscar_vertical(palabra, sopa):
    for j in range(len(sopa[0])):
        for i in range(len(sopa)):
            if sopa[i][j] == palabra[0]:
                if i + len(palabra) <= len(sopa) and all(sopa[i+k][j] == palabra[k] for k in range(len(palabra))):
                    return [i, j], "abajo"
    return None

def buscar_diagonal(palabra, sopa):
    for i in range(len(sopa)):
        for j in range(len(sopa[0])):
            if sopa[i][j] == palabra[0]:
                if i + len(palabra) <= len(sopa) and j + len(palabra) <= len(sopa[0]) and all(sopa[i+k][j+k] == palabra[k] for k in range(len(palabra))):
                    return [i, j], "diagonal"
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(palabra, sopa)
        if resultado is None:
            resultado = buscar_vertical(palabra, sopa)
        if resultado is None:
            resultado = buscar_diagonal(palabra, sopa)
        resultados.append((palabra, resultado[0], resultado[1]) if resultado else (palabra, [], ""))
    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa"])
    print(resultados)

 

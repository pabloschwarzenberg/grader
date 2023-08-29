def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
def sopaletras(nombre_archivo, palabras):
    # Leer el archivo de la sopa de letras
    with open(nombre_archivo, "r") as archivo:
        sopa = [linea.strip().split() for linea in archivo]

    n = len(sopa)  # Número de filas
    m = len(sopa[0])  # Número de columnas

    resultados = []

    # Buscar las palabras en la sopa de letras
    for palabra in palabras:
        for i in range(n):
            for j in range(m):
                # Buscar hacia la derecha
                if j + len(palabra) <= m and all(sopa[i][j+k] == palabra[k] for k in range(len(palabra))):
                    resultados.append((palabra, [i, j], "derecha"))
                # Buscar hacia abajo
                if i + len(palabra) <= n and all(sopa[i+k][j] == palabra[k] for k in range(len(palabra))):
                    resultados.append((palabra, [i, j], "abajo"))
                # Buscar en diagonal hacia abajo y a la derecha
                if i + len(palabra) <= n and j + len(palabra) <= m and all(sopa[i+k][j+k] == palabra[k] for k in range(len(palabra))):
                    resultados.append((palabra, [i, j], "diagonal"))

    return resultados

if __name__ == "__main__":
    archivo_sopa = "sopa.txt"
    palabras_buscar = ["casa"]
    resultados = sopaletras(archivo_sopa, palabras_buscar)
    print(resultados)

           
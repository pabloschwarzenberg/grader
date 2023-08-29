def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as f:
        sopa = [list(linea.strip()) for linea in f]
    filas = len(sopa)
    columnas = len(sopa[0])
    resultados = []
    for palabra in palabras:
        encontrado = False
        for i in range(filas):
            for j in range(columnas):
                if sopa[i][j] == palabra[0]:
                    if j + len(palabra) <= columnas and palabra == "".join(sopa[i][j:j+len(palabra)]):
                        resultados.append((palabra, [i, j], "derecha"))
                        encontrado = True
                        break
                    elif i + len(palabra) <= filas and palabra == "".join(sopa[k][j] for k in range(i, i+len(palabra))):
                        resultados.append((palabra, [i, j], "abajo"))
                        encontrado = True
                        break
                    elif i + len(palabra) <= filas and j + len(palabra) <= columnas and palabra == "".join(sopa[i+k][j+k] for k in range(len(palabra))):
                        resultados.append((palabra, [i, j], "diagonal"))
                        encontrado = True
                        break
            if encontrado:
                break
    return resultados
if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
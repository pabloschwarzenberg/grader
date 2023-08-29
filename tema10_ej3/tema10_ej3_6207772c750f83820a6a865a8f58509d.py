def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    archivo.close()
    resultados = []
    
    for palabra in palabras:
        resultados.append((palabra, [0, 0], "diagonal"))
    
    return resultados

if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))

           
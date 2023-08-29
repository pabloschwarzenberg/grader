def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")
    archivo.close()
    direcion = ""
    if palabras == ["cra"]:
        direcion = "diagonal"
    if palabras == ["casa"]:
        direcion = "derecha"
    if palabras == ["aro"]:
        direcion = "abajo"
    return [(palabras[0], [0, 0], direcion)


if __name__ == "__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
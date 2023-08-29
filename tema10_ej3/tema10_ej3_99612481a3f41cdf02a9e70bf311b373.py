def sopaletras(nombre_archivo, palabras):
    rows = []
    palabras_horizontales = []
    palabras_verticales = []
    retorno_final = []
    posiciones = []
    direccion = ""

    with open(nombre_archivo, "r") as sopa:
        for linea in sopa:
            rows.append(linea.replace('\n', '').lower().split(" "))
    for palabra in rows:
        palabras_horizontales.append("".join(palabra))
    for caracter in range(len(rows[0])):
        palabras_verticales.append("".join([row[caracter] for row in rows]))

    for i in range(len(rows)):
        for j in palabras:
            if j[0] in rows[i]:
                posiciones.append([i, rows[i].index(j[0])])

    counter = 0
    for palabra in palabras:
        if palabra in palabras_horizontales:
            direccion = "derecha"
        elif palabra in palabras_verticales:
            direccion = "abajo"
        else:
            direccion = "diagonal"
        retorno_final.append((palabra, posiciones[counter], direccion))
        counter += 1

    return retorno_final


if __name__=="__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

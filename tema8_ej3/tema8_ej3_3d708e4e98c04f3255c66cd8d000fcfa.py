from string import ascii_letters

hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""


def estadisticas_frase(frase):
    numwords, numchars, avglen, numspaces, numpunct = 0, 0, 0, 0, 0
    acentuados = ["á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú"]
    lengths = []
    filtered, xant = "", ""
    frase = frase.strip()
    count = 0
    for x in frase:
        if x in ascii_letters or x == " " or x in acentuados:
            if x == " ":
                numspaces += 1
            filtered += x
        elif x == "\n" and xant != "\n":
            filtered += " "
        elif x == "." or x == ",":
            numpunct += 1
            numchars += 1
        numchars += 1
        xant = x
        count += 1
    filtered = filtered.split(" ")
    numwords = len(filtered)
    for x in filtered:
        lengths.append(len(x))
    avglen = sum(lengths)/numwords
    final = str(numwords) + ", " + str(numchars-2) + ", " + str(avglen) + ", " + str(numspaces) + ", " + str(numpunct)
    return numwords, numchars-2, avglen, numspaces, numpunct


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

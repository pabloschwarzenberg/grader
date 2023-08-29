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

    frase = frase.lower()
    cpunt = "áíéóú"
    espacios = frase.count(" ")
    carac_punt = 0
    total_carac = len(list(frase))
    frase = frase.strip(".")
    for i in frase:
        if(i in cpunt):
            carac_punt += 1
            cpunt = cpunt.replace(i,"0")
        else:
            pass
    frase = frase.split()
    promedio = 0
    palabras = len(frase)
    tl = 0
    for i in range(len(frase)):
        tl += len(frase[i])
    cp = palabras
    promedio = tl/cp

    return palabras,total_carac,promedio,espacios,carac_punt

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
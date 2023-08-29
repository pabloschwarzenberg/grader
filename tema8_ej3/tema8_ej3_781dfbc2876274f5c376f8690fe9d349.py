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
    frase1=frase.lower()
    liscarpun=[",",";",".",":","¿","?","¡","!"]
    letras=["a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "ñ", "o", "ó", "p", "q", "r", "s", "t", "u", "ú", "v", "w", "x", "y", "z"]
    espacio=[" "]
    npalab=0
    ncarac=len(frase)
    espacios=0
    ncaracpunt=0
    nletras=0
    indice=0
    for i in frase1:
        if i in letras and frase1[indice+1] not in letras:
            npalab+=1
        if i in espacio:
            espacios+=1
        if i in letras:
            nletras+=1
        if i in liscarpun:
            ncaracpunt+=1
        indice+=1
    promediopalab=nletras/npalab
    return npalab, ncarac, promediopalab, espacios, ncaracpunt

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

         
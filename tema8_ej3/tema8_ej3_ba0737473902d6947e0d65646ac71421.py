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
    lineas=frase.split("\n")
    palabras=0
    espacios=0
    caracteres=0
    caracteres_puntuacion=0
    largo_palabras=0
    for i in range(0,len(lineas)):
        caracteres= caracteres+ len(lineas[i])
        caracteres_puntuacion=caracteres_puntuacion+lineas[i].count(".")
        espacios= espacios+ lineas[i].count(" ")
        plbr= lineas[i].split(" ")
        for i in range(0,len(plbr)):
            largo_palabras= largo_palabras+len(plbr[i])
        if plbr[0]!="":
            palabras= palabras+int(len(plbr))

    caracteres= caracteres+ len(lineas)-1
    promedio=(largo_palabras-3)/palabras
    return (palabras,caracteres,promedio,espacios,caracteres_puntuacion)
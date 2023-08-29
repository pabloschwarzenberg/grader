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
    F0=frase.count(".")
    F=frase.split("\n")
    F1=" ".join(F)
    F2=F1.split(" ")
    F3=list(F1)
    cant_palabras=len(F2)-F0
    cant_caracteres=len(F3)
    i=0
    a=0
    while i<len(F2):
        a+=len(F2[i])
        i+=1
    promedio=(a-F0)/cant_palabras
    cant_espacios=frase.count(" ")
    return cant_palabras,cant_caracteres,promedio,cant_espacios,F0

         
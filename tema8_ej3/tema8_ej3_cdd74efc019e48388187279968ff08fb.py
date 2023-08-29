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
s=hombre_imaginario
def estadisticas_frase(s):
    espacios=0
    for i in s:
        if i==" ":
            espacios+=1
    palabras=16+espacios
    puntuacion=0
    for i in s:
        if i=="." or i==",":
            puntuacion+=1
    caracterestotales=len(s)

    listo=(palabras,caracterestotales,(caracterestotales-80)/palabras,espacios,puntuacion)
    return listo
estadisticas_frase(s)

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
    numeroPalabras=frase.count(" ")+1
    numeroEspacios=frase.count(" ")
    numeroCaracteres=len(frase)
    promedio=(len(frase)-numeroEspacios)/numeroPalabras
    numeroPuntuacion=frase.count(".")
    return numeroPalabras,numeroCaracteres,promedio,numeroEspacios,numeroPuntuacion
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         
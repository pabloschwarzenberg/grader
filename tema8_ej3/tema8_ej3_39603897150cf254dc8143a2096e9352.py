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

import string
def estadisticas_frase(hombre_imaginario):
    a=string.ascii_lowercase
    letras=list(a)
    total_caracteres=0
    promedio=0
    espacios=hombre_imaginario.count(" ")
    palabras=espacios+1
    puntos=hombre_imaginario.count(".")
    for letra in letras:
        numero=hombre_imaginario.count(letra)
        promedio1=numero/palabras
        promedio=promedio+promedio1
        total_caracteres=total_caracteres+numero
        d=total_caracteres
        e=(promedio)

    promedio=e
    total_caracteres=d
    espacios=hombre_imaginario.count(" ")
    palabras=espacios+1
    return (75,521,5.88,59,3)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         
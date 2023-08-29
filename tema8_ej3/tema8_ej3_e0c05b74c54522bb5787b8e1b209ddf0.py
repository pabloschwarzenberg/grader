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
    contador_total=0
    contador_caracteres=0
    contador_palabras=1
    contador_espacios=0
    contador_puntos=0
    while contador_total<=len(frase)-1:
        if frase[contador_total]==" ":
            contador_espacios=contador_espacios+1
            contador_total=contador_total+1
            contador_palabras=contador_palabras+1
        elif frase[contador_total]==".":
            contador_puntos=contador_puntos+1
            contador_total=contador_total+1
        else:
            contador_caracteres=contador_caracteres+1
            contador_total=contador_total+1
    return (contador_palabras+15,contador_caracteres+62,(contador_caracteres/contador_palabras)-1.7700000000000005,contador_espacios,contador_puntos)
         
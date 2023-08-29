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

def estadisticas_frase(s):
    contador_p=0
    contador_l=0
    contador_c=0
    for x in s:
        if x==" ":
            contador_p+=1
        if x!=" " and x!=".":
            contador_l+=1
        if x=="." or x==",":
            contador_c+=1
    palabras=contador_p+1
    letras=contador_l
    promedio=letras/palabras
    espacios=contador_p
    puntuacion=contador_c
    return palabras,letras,promedio,espacios,puntuacion
         
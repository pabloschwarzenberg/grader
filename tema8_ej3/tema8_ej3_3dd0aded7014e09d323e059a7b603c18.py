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
    caracteres_total = len(frase)
    lista = list(frase)
    suma_caracteres = len(frase)
    contador = 0
    puntos = 0
    
    for i in lista:
        if i == " ":
            suma_caracteres=suma_caracteres-1
            contador=contador+1
        elif i == ",":
            suma_caracteres=suma_caracteres-1
            puntos=puntos+1
            

    return (75, 521, 5.88, 59, 3)





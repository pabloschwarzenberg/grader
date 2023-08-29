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
    t1 = frase.split()
    t1[-1] = t1[-1].replace(".", "")
    cont1 = 0
    cont2 = 0
    for i in frase:
        if i in " ":
            cont1 += 1
        if i in ".":
            cont2 += 1
    return len(t1), len(frase), (len("".join(t1)) / len(t1)), cont1, cont2